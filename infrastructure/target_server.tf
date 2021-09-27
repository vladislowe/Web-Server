provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "Target_server" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = var.key_name

  tags = {
    Name = "Target_server"
  }
}
