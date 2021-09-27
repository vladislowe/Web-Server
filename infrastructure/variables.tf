variable "ami" {
  description = "Ubuntu Server 20.04 LTS"
  type        = string
  default     = "ami-05f7491af5eef733a"
}

variable "instance_type" {
  description = "Just instance type"
  type        = string
  default     = "t2.micro"
}

variable "key_name" {
  description = "Name of the SSH key"
  type        = string
  default     = "vlads-key-Frankfurt"
}

