// USING Zig 0.13.0

const std = @import("std");

pub fn gpa() std.mem.Allocator {
    var gpalloc = std.heap.GeneralPurposeAllocator(.{}){};
    return comptime gpalloc.allocator();
}

pub fn readFile(filename: []const u8, allocator: std.mem.Allocator) ![]u8 {
    const file = try std.fs.cwd().openFile(filename, .{ .mode = .read_only });
    defer file.close();

    const stat = try file.stat();
    const buff = try file.readToEndAlloc(allocator, stat.size);
    return buff;
}

pub fn getLines(filename: []const u8, allocator: std.mem.Allocator) !std.ArrayList([]const u8) {
    const buff = try readFile(filename, allocator);
    defer allocator.free(buff);

    var lines = std.ArrayList([]const u8).init(allocator);

    var split_iter = std.mem.splitSequence(u8, buff, "\n");

    while (split_iter.next()) |line| {
        try lines.append(try lines.allocator.dupe(u8, line));
    }

    return lines;
}
