provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "Main_server" {
  ami               = var.ami
  instance_type     = var.instance_type
  key_name          = var.key_name
  availability_zone = "eu-central-1b"

  user_data = file("main_server_user_data.sh")
  tags = {
    Name = "Jenkins_controller"
  }
}

resource "aws_instance" "Jenkins_agent" {
  ami                  = var.ami
  instance_type        = var.instance_type
  key_name             = var.key_name
  availability_zone    = "eu-central-1b"
  iam_instance_profile = "terraform-jenkins-role"

  user_data = file("jenkins_agent_user_data.sh")
  tags = {
    Name = "Jenkins_agent"
  }
  depends_on = [aws_instance.Main_server]
}
