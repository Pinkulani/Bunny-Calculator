#![allow(non_snake_case)]
use std::io;

fn Input() -> (i64, i64) {
    let mut A = String::new();
    let mut B = String::new();

    println!("Type Number 1: ");
    io::stdin().read_line(&mut A).expect("Reading error");
    let A: i64 = A.trim().parse().expect("Invalid number!");

    println!("Type Number 2: ");
    io::stdin().read_line(&mut B).expect("Reading error");
    let B: i64 = B.trim().parse().expect("Invalid number!");

    (A, B)
}

fn Output(Result: i64) {
    println!("Your result is: {}", Result);
}

fn Adding(A: i64, B: i64) -> i64 {
    A + B
}

fn Subtracting(A: i64, B: i64) -> i64 {
    A - B
}

fn Multiplication(A: i64, B: i64) -> i64 {
    A * B
}

fn Division(A: i64, B: i64) -> i64 {
    A / B
}

fn main() {
    println!("1 = Adding | 2 = Subtracting | 3 = Multiplication | 4 = Division");
    println!("Which type?");

    let mut Selection = String::new();
    io::stdin().read_line(&mut Selection).expect("Reading error");
    let Selection: i64 = Selection.trim().parse().expect("Invalid number!");

    let (A, B) = Input();
    let Result = match Selection {
        1 => Adding(A, B),
        2 => Subtracting(A, B),
        3 => Multiplication(A, B),
        4 => Division(A, B),
        _ => { println!("Invalid option!");
               return;
        }
    };

    Output(Result);
}
