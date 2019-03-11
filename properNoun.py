def properNounCorrection(noun):
	# pretty straightforward . slice first word make it upper. Make everything else lower. Concat !
    return noun[0].upper()+noun[1:].lower()

