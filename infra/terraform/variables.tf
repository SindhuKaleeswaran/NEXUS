variable "aws_region" {
  type    = string
  default = "us-west-2"
}

variable "availability_zones" {
  type    = list(string)
  default = ["us-west-2a", "us-west-2b"]
}

