use std::fs::File;
use std::io::{Write};

#[derive(Debug)]
struct Entry {
    host: String,
    user: String,
    port: u16,
    identity: String,
}

impl Entry {
    fn sessiontime(&self, interval: u8, countmax: u8) 
                    -> std::io::Result<()> {
        let mut file = File::options().append(true).open("config")?;
        write!(file, "Host *\n");
        write!(file, "\tServerAliveInterval {}\n", interval);
        write!(file, "\tServerAliveCountMax {}\n\n", countmax);
        Ok(())
    }
}

fn main() {
    let ent1 = Entry { 
        host: String::from("do.lab"),
        user: String::from("boink"),
        port: 9993,
        identity: String::from("/key/store/key")
    };
    
    config_print(&ent1).expect("Error writing basic config");
    ent1.sessiontime(180, 3).expect("Error writing session config");
    // println!("ent1 is {:#?}", ent1);
}

fn config_print(ent: &Entry) -> std::io::Result<()> {
    let mut file = File::create("config")?;

    write!(file, "Host {}\n", ent.host);
    write!(file, "\tUser {}\n", ent.user);
    write!(file, "\tPort {}\n", ent.port);
    write!(file, "\tIdentityFile {}\n\n", ent.identity);
    Ok(())
}