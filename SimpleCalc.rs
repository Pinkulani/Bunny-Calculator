use std::io;

fn main() {
	println!("Choose option: ");
	let mut Option = String::new();
	io::stdin().read_line(&mut Option).expect("Invalid input!");
	println!("Choosen option:  {}", Option);
}
	
