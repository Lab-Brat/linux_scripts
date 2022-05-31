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
  let (ip, octet_count) = validate_ip(&ipv4);
  if octet_count == 3 {
    println!("{} is a valid IP address", ip);
  } else if octet_count == -1 {
    println!("{}", ip)
  } else {
    println!("Error: Too few octets");
  }
}

fn validate_ip(ipv4: &str) -> (String, i8) {
  let bytes = ipv4.as_bytes();
  let mut octet_count = 0_i8;
  let mut j = 0;

  for (i, &item) in bytes.iter().enumerate() {
    let cc = item as char;
    // only allow numbers and .
    if cc.is_numeric() || cc == '.' {
      if item == b'.' {
        octet_count = &octet_count + 1;
  
        // check if an octet is larger than 255 or too mant octets
        let octet = &ipv4[j..i].parse::<i32>().unwrap();
        j = i+1;
        if octet > &255 {
          return (String::from("Error: Octet is larger than 255"), -1);
        } else if octet_count > 3 {
          return (String::from("Error: Too many octets"), -1);
        }
      }
    } else {
      return (String::from("Error: wrong characher in IP address"), -1);
    }

  }
  (String::from(ipv4), octet_count)
}
