text = "X-DSPAM-Confidence:    0.8475";
first = text.find('0')
fnum = float(text[first:])
print(fnum)
