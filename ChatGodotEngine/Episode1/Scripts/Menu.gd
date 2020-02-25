extends Control
func _ready():
	pass


func _on_Host_pressed():
	print("Host")


func _on_Join_pressed():
	if $IP.text.is_valid_ip_address():
		pass
	else:
		$IP.text="Invalide !"
	
