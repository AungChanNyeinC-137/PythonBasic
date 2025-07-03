guest_list = [
'Monica Geller',
'Chandler Bing',
'Phoebe Buffay',
'Joey Tribbiani',
'Rachel Green',
'Ross Geller',
]
sorry_statement = f"We'll miss you at dinner! We're sorry '{guest_list[2]}' can't make it, but we hope to see you another time soon."
new_statement = f"'Gunter' will join the party instead of '{guest_list[2]}', Let's welcome him!"
print(sorry_statement)
print(new_statement)
guest_list.pop(2)
guest_list.append("Gunther")

new_invitation_message = "You're warmly invited to join us for dinner. We'd love to share a meal and catch up!"
print(guest_list[0] + ", "+ new_invitation_message)
print(guest_list[1] + ", "+ new_invitation_message)
print(guest_list[2] + ", "+ new_invitation_message)
print(guest_list[3] + ", "+ new_invitation_message)
print(guest_list[4] + ", "+ new_invitation_message)
print(guest_list[5] + ", "+ new_invitation_message)