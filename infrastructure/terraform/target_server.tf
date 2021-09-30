provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "Target_server" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = var.key_name
  availability_zone = "eu-central-1b"
  user_data = file("user_data.sh")

  tags = {
    Name = "Target_server"
  }
}

output "instance_ip_addr" {
  value = aws_instance.Target_server.public_ip
}
