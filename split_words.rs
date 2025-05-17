use std::fs::File;
use std::collections::BTreeSet;
use std::io::{BufReader, BufRead, Error};
use std::any::type_name;

fn print_type_of<T>(_: &T) {
    println!("The type is: {}", type_name::<T>());
}
fn main() -> Result<(), Error> {
    let path = "corpus.txt";
    let mut bbooks = BTreeSet::new();
    let input = File::open(path)?;
    let buffered = BufReader::new(input);
    let mut lines = Vec::new();
    lines = buffered.lines().map(|line| line.unwrap()).collect();
    let all_str = &lines[0];
    let items: Vec<&str> = all_str.split(" ").collect();
    for i in &items {
        // println!("{}", i);
        if !bbooks.contains(&i){
            bbooks.insert(i);
        }
    }
    for book in &bbooks {
      let str1 = "";
      let a = **book;
      if a.eq(str1) {
        println!("[unk]");
      } else {
        println!("{}",book);
      }
    }
    Ok(())
}