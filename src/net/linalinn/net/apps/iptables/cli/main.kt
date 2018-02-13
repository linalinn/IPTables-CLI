package net.linalinn.net.apps.iptables.cli
import net.linalinn.net.apps.iptables.cli.Command
import kotlin.system.*

fun main(args: Array<String>) {
	val c = Command()
	for (i in 0..args.size-1) {
		when (args[i]){
			"-dip"		-> c.setdIP(args[i+1])
            "-dport" 	-> c.setdIP(args[i+1])
            "-to" 		-> c.setdIP(args[i+1])
            "-IN" 		-> c.setdIP(args[i+1])
            "--add-APP" -> println("--add-APP")
			"--wizard"	-> wizard()
            else -> println("else")
		}
	}
	println(c.verify())
}

fun wizard(){
	println("Destination IP of Package * for all")
	var dIP = readLine()
	println("Destination Port of Package * for all")
	var dport = readLine()
	println("IP and/or Port Package to send to")
	var to = readLine()
	println("Chain (IN/OUT)")
	var chain = readLine()
	println(Command().verify())
	exitProcess(0)
}