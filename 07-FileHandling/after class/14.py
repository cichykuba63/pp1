import re

statement = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Bibendum est ultricies integer quis auctor elit sed vulputate mi. Elementum pulvinar etiam non quam lacus suspendisse faucibus interdum posuere. Vestibulum morbi blandit cursus risus at ultrices mi tempus imperdiet. Vel risus commodo viverra maecenas accumsan lacus vel facilisis volutpat. Sem et tortor consequat id porta nibh."

words = re.findall("\w{6,}", statement)

for word in words:
    print(word)