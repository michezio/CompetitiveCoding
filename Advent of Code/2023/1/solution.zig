// USING Zig 0.13.0

const std = @import("std");
const common = @import("common");

var gpalloc = std.heap.GeneralPurposeAllocator(.{}){};
const gpa = gpalloc.allocator();

const digits = [9][]const u8{ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
const digits_reverse = [9][]const u8{ "eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin" };

pub fn main() !void {
    const buff = try common.readFile("input.txt", gpa);
    defer gpa.free(buff);

    var lines = try common.getLines(buff, gpa);
    defer lines.deinit();

    const sol_1 = solve_part_1(lines);
    std.debug.print("Answer part 1: {d}\n", .{sol_1});

    const sol_2 = solve_part_2(lines);
    std.debug.print("Answer part 2: {d}\n", .{sol_2});
}

fn solve_part_1(lines: std.ArrayList([]u8)) usize {
    var cumulative_sum: usize = 0;

    for (lines.items) |line| {
        const num = solve_for_line(line);
        //std.debug.print("{d}\t{s}\n", .{ num, line });
        cumulative_sum += num;
    }

    return cumulative_sum;
}

fn solve_part_2(lines: std.ArrayList([]u8)) usize {
    var cumulative_sum: usize = 0;

    for (lines.items) |line| {
        const tline = transform_line(line);
        const num = solve_for_line(tline);
        //std.debug.print("{d}\t{s}\n", .{ num, line });
        cumulative_sum += num;
    }

    return cumulative_sum;
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

    return number;
}

fn transform_forward(lineb: []u8, words: [9][]const u8) []u8 {
    var line = lineb[0..];

    find_first: while (line.len >= 3) {
        if (std.ascii.isDigit(line[0])) {
            break;
        }
        for (words, 1..words.len + 1) |digit, n| {
            if (digit.len > line.len) continue;
            for (0..digit.len) |i| {
                if (line[i] != digit[i]) {
                    break;
                }
            } else {
                line[0] = '0' + @as(u8, @truncate(n));
                line = line[digit.len..];
                break :find_first;
            }
        } else {
            line = line[1..];
        }
    }

    return lineb;
}

fn transform_line(lineb: []u8) []u8 {
    var line = transform_forward(lineb, digits);
    std.mem.reverse(u8, line);
    line = transform_forward(line, digits_reverse);
    std.mem.reverse(u8, line);

    return line;
}

test "solve_for_line" {
    try std.testing.expectEqual(12, solve_for_line("1abc2"));
    try std.testing.expectEqual(38, solve_for_line("pqr3stu8vwx"));
    try std.testing.expectEqual(15, solve_for_line("a1b2c3d4e5f"));
    try std.testing.expectEqual(77, solve_for_line("treb7uchet"));
}

test "transform_forward" {
    var line1 = "onetwothree".*;
    const line1_t = transform_forward(&line1, digits);
    try std.testing.expectEqualStrings("1netwothree", line1_t);

    var line2 = "theeighthree4fiv".*;
    const line2_t = transform_forward(&line2, digits);
    try std.testing.expectEqualStrings("the8ighthree4fiv", line2_t);
}

test "transform_line" {
    var line1 = "onetwothreefourfivesixseveneightnine".*;
    const line1_t = transform_line(&line1);
    try std.testing.expectEqualStrings("1netwothreefourfivesixseveneightnin9", line1_t);

    var line2 = "threeighthree4fiv".*;
    const line2_t = transform_line(&line2);
    try std.testing.expectEqualStrings("3hreeighthree4fiv", line2_t);
}

test "solve_part_1" {
    const test_input =
        \\1abc2
        \\pqr3stu8vwx
        \\a1b2c3d4e5f
        \\treb7uchet
    ;
    const lines = try common.getLines(test_input, gpa);
    defer lines.deinit();
    const sol_1 = solve_part_1(lines);
    try std.testing.expectEqual(142, sol_1);
}

test "solve_part_2" {
    const test_input =
        \\two1nine
        \\eightwothree
        \\abcone2threexyz
        \\xtwone3four
        \\4nineeightseven2
        \\zoneight234
        \\7pqrstsixteen
    ;
    const lines = try common.getLines(test_input, gpa);
    defer lines.deinit();
    const sol_2 = solve_part_2(lines);
    try std.testing.expectEqual(281, sol_2);
}
