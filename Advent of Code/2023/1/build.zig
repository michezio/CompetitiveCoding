// USING Zig 0.13.0

const std = @import("std");

pub fn build(b: *std.Build) void {
    const common_module = b.addModule("../common.zig", .{
        .root_source_file = b.path("../common.zig"),
    });

    const solution_exe = b.addExecutable(.{
        .name = "solution",
        .root_source_file = b.path("solution.zig"),
        .target = b.standardTargetOptions(.{}),
        .optimize = b.standardOptimizeOption(.{}),
    });

    solution_exe.root_module.addImport("../common.zig", common_module);

    b.installArtifact(solution_exe);

    const run_solution = b.addRunArtifact(solution_exe);
    const run_step = b.step("run", "Run the solution");
    run_step.dependOn(&run_solution.step);
}
