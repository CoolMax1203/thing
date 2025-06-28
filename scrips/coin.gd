extends Area2D

@onready var game_m: Node = %GameM
@onready var animation_player: AnimationPlayer = $AnimationPlayer


func _on_body_entered(body: Node2D) -> void:
	game_m.add_point()
	animation_player.play("pickup")
