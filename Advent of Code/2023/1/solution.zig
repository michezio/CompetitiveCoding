// USING Zig 0.13.0

const std = @import("std");
const common = @import("../common.zig");

pub fn main() !void {
    var gpalloc = std.heap.GeneralPurposeAllocator(.{}){};
    const gpa = gpalloc.allocator();

    const lines = try common.getLines("input.txt", gpa);
    defer lines.deinit();

    const sol_1 = solve_part_1(lines);
    std.debug.print("Answer part 1: {d}\n", .{sol_1});

    const sol_2 = solve_part_2(lines);
    std.debug.print("Answer part 2: {d}\n", .{sol_2});
}

fn solve_for_line(line: []const u8) usize {
    var digit_1: u8 = 0;
    var digit_2: u8 = 0;
    var linev = line;

    for (linev, 0..) |char, i| {
        if (std.ascii.isDigit(char)) {
            linev = linev[i..];
            digit_1 = char - '0';
            break;
        }
    }

    for (0..linev.len) |i| {
        const char = linev[linev.len - 1 - i];
        if (std.ascii.isDigit(char)) {
            digit_2 = char - '0';
            break;
        }
    }

    const number: u8 = digit_1 * 10 + digit_2;

    std.debug.print("{d}\t{s}\n", .{ number, line });

    return number;
}

fn solve_part_1(lines: std.ArrayList([]const u8)) usize {
    var cumulative_sum: usize = 0;

    for (lines.items) |line| {
        cumulative_sum += solve_for_line(line);
    }

    return cumulative_sum;
}

fn solve_part_2(lines: std.ArrayList([]const u8)) usize {
    var cumulative_sum: usize = 0;

    for (lines.items) |line| {
        // TODO: modify line then solve
        cumulative_sum += solve_for_line(line);
    }

    return cumulative_sum;
}
