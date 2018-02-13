package net.linalinn.net.apps.iptables.cli

class Command {
	private var dIP: String    = ""
	private var dport: String  = ""
	private var to: String     = ""
	private var chain: String  = ""
	
	constructor(){
		
	}
	constructor(dIP:String, dport:String, to:String, chain:String){
		this.dIP = dIP
		this.dport = dport
		this.to = to
		this.chain = chain		
	}
	
	fun setdIP(dIP:String){
		this.dIP = dIP
	}
	
	fun setdport(dport:String){
		this.dport = dport
	}
	
	fun setto(to:String){
		this.to = to
	}
	
	fun setchain(chain:String){
		when (chain){
			"IN"  -> this.chain = "IN"
			"OUT" -> this.chain = "OUT"
		}
	}
	fun verify():Boolean{
		if (dIP != "" || dport != "" ){
			if (to != "" && chain != ""){
				return true;
			}
		}
		return false;
	}
	
}