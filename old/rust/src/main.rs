use std::env;

struct parameter{
    paratype: String,
    value: String,
}


fn main() {
    let args: Vec<_> = env::args().collect();
    let mut para : Vec<parameter> = Vec::new();
    let  mut a : String ;
    for i in 0..args.len(){
        match args[i].as_ref() {
            "-dip" => para.push(parameter {paratype:"dip".to_ascii_lowercase(),value: (&args[i+1]).to_ascii_lowercase()}),
            "-dport" => para.push(parameter {paratype:"dport".to_ascii_lowercase(),value: (&args[i+1]).to_ascii_lowercase()}),
            "-to" => para.push(parameter {paratype:"to".to_ascii_lowercase(),value: (&args[i+1]).to_ascii_lowercase()}),
            "-OUT" => para.push(parameter {paratype:"chain".to_ascii_lowercase(),value: "OUT".to_ascii_lowercase()}),
            "-IN" => para.push(parameter {paratype:"chain".to_ascii_lowercase(),value:"IN".to_ascii_lowercase()}),
            "--add-APP" => println!("ADD-APP"),
            _ => println!("BUG")

        }

    }
    println!("{:?} {}", para[1].paratype , para[1].value);
    if args.len() > 1 {
        let mut last = String::new();
        for arg in &args {
            //println!("{:?}",arg );
        }
    }
}

fn verifycommand(para: Vec<parameter>){
    

}
