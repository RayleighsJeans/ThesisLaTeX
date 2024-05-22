This is the README for the bolometer LabView VI.

$ ########################################################################## $
### Things happening in the current commit of the VI:

	1 - a - Use all channels or a selection of to estimate/calculate the
			total irradiated power from the plasma for the helium
			beam diagnostic
		b - UI interface to input the channels/channel numbers
		c - single channel output alongside using the voltage or power

	2 - Appropriate scale for the output voltage and distributing that
		to the partnering diagnostic. For example, 10 MW ~ 10 V.
		Also one can specify individual factor the signal is supposed
		to be multiplied with so it fits the full P_rad better.

	3 - Create an array and make an UI interface for such to input the
		weighting factors to be used with the channel selection when
		calculating P_rad; get geomtry factors from file.

	4 - a - plot of P_rad estimate from the transmitted samples
		b - Add the "true" P_rad after the shot to this plot from both cameras
		c - Writes the full P_rad and the estimate plus single channel
			feedback to the archive.

	5 - a - Make the current configuration available via a file that can be
			saved and loaded via a *.json or comparable.
		b - This has to be appended on to the existing parameter upload
			and/or the upload of the P_rad estimate.
		c - all uploads are linked to the storage of local json files,
			meaning that also the saving fails if the upload fails

	6 - Use internal epoch timing as trigger to properly store
		files in archive when testing

	7 - double channel voltage output via the references handed over to the
		hReadChannelsUandP for single values of channel and P_rad;
		also possible to skip feedback inside DAQ, button on front panel

	8 - skipping first XXXX samples to DAQ because step in signal from
		pins selection needs to be evaded; floating potential the first few
		dozen famples

	9 - Upload of all the things from the VI created; also adjusted signals
		used for feedback etc.

	10 - selectable mode at which the acquisition is run can be selected with
		 a bit switch on the front panel

	11 - redone calibration sequence the properly reflect the foil
		 characteristics, including 0.4ms sampling correctly set
		 and fitting enhanced; plots over all channels with any parameter

	12 - real sampling time, not just rough approx. from FreqSel.vi
		 with chop/nonchop mode and equation from masterclock
		 more possible rates to chose from

$ ########################################################################## $
### Things that are done currently by the VI:

	Upload of the acquired signals from the bolometer itself.
	Calculation of the power of each detector.
	Upload of the corresponding parameter data to the archive.
	Measurement, triggering, trigger acquisition, heat up, pre-measurement and
	calibration.

	New:
		* Loading of the kbolott and volume data from the torus_... *.dat
		  files reference passsage to and from a subVI.

		* loading from file and input individual DAC/range settings
		  for channels

		* loading from file and input of channel selection for real
		  time P_rad

		* calculation of P_rad sample in sub routine
		  hReadChannels-UandP-2018.vi

		* referencing and output of said sample to main W7X VI

		* acquisition of 10 sampels that are stored in a 11 sequence array
		  where the first one is dedicated to the average of said 10
		  --> averaging of 10 samples to one float

		* if sample greater than 10, first (second in array) element is
		  replaced with new sample that was most recently acquired

		* calculations with given kbolott and volume data to one P_rad
		  estimate

		* analog voltage output via AO0/1 of NI PCIe 6321(R) corresponding
		  to the current P_rad sample and single channel signal

