use std::io;

fn main() {
  println!("Please input an IPv4 address: ");

  let mut ipv4 = String::new();

  // read input and remove newline symbol in the end
  io::stdin().read_line(&mut ipv4)
      .expect("Failed to read line");
  ipv4.pop();
  ipv4.pop();
  
  // validate IP address and print output
  let is_ip = val_ip(&ipv4);
  if is_ip == true { println!("{} is a valid IP", ipv4); }
  else { println!("{} is a NOT valid IP", ipv4); }
}

fn val_ip(ipv4: &str) -> bool {
  // check the octet count and it's range
  if check_symbols(ipv4) == true {

    let split = ipv4.split('.');
    let mut count = 0;

    for s in split {
      count += 1;
      let octet = s.parse::<u16>().unwrap();
      if octet > 255 { return false } 
    }
    if count == 4 { return true }
  }
  return false
}

fn check_symbols(ipv4: &str) -> bool {
  // check if input only contains . and numbers
  for cc in ipv4.chars() {
    if cc=='.' || cc.is_numeric() { () } 
    else { return false }
  }
  return true
}
