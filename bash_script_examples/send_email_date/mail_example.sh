#!/bin/bash
Recipient=”indra0102thetiger@gmail.com”
Subject=”Greeting”
Message=”Welcome to our site”
`mail -s $Subject $Recipient <<< $Message`
