// USING Zig 0.13.0

const std = @import("std");

pub fn build(b: *std.Build) void {

    // COMMON MODULE

    const common_module = b.addModule("common", .{
        .root_source_file = b.path("../common.zig"),
    });

    // EXECUTABLE

    const solution_exe = b.addExecutable(.{
        .name = "solution",
        .root_source_file = b.path("solution.zig"),
        .target = b.standardTargetOptions(.{}),
        .optimize = b.standardOptimizeOption(.{}),
    });

    solution_exe.root_module.addImport("common", common_module);

    const run_solution = b.addRunArtifact(solution_exe);
    const run_step = b.step("run", "Run the solution");
    run_step.dependOn(&run_solution.step);

    b.installArtifact(solution_exe);

    // UNIT TESTS

    const unit_tests = b.addTest(.{
        .name = "test",
        .root_source_file = b.path("solution.zig"),
    });

    unit_tests.root_module.addImport("common", common_module);

    const run_unit_tests = b.addRunArtifact(unit_tests);
    const test_step = b.step("test", "Run unit tests");
    test_step.dependOn(&run_unit_tests.step);
}
