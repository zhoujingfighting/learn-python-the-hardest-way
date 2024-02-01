# @always_inline
fn add(a: Int, b: Int) -> Int:
    return a + b
var a = 1
fn main() raises -> None:
    a += add(1, 2)