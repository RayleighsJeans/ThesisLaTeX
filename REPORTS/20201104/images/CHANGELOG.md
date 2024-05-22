Initial Commit brings the LabView VI currently in use at the stellarator W7-X.
Changes TODO might be the fast feedback setup, the early heating/data
acquisition and others.

$ ########################################################################## $
### MAIN VI CHANGELOG (W7XBolo2017_Flo.vi)

    04/15/2018
    ----------
    v1.0.0

    04/23/2018
    ----------
    v1.0.1
    ++ cleaned / tidy up front panel (user interface)
    ++ added epoch time debug to the trigger panel in 'Control Tab 4'
    ++ made the T1-T0 time accessible through 'Control Tab 4' / trigger panel

    04/25/2018
    ----------
    v1.0.5
    ++ added necessary files to directory for P_rad calculation
    ++ real time P_rad plot window added, no connection yet
    ++ wired upload of calculated channel power through and to archive
         -----> SEE ISSUE 4.C, partially cleared !$*%&
    ++ created test vi to check file import and write test.dat

    04/27/2018
    ----------
    v1.1.0
    ++ local variable of kbolott_and_volume to pass on to the main vi
       either load from file or via routine where location and subfiles
       are specified
    ++ versioning/control via LabView (comments and version number
       included)
    ++ DAC/DAQ file load or input via the UI

    05/03/2018
    ----------
    v1.1.5
    ++ fixed all the file loads, inputs and switches for DAC settings, ranges
       kbolott and volume data and so on
    ++ switch in load_kbolott_volume.vi for file paths in loading,
       diagnostics or VPC
    ++ found how to pass on variables LIVE between VIs --> references
       very easy to work with on the UI (drag and drop)
       --> next up is the channeling to the other PCIe card and the actual
           on the fly P_rad calculation

    05/23/2018
    ----------
    v1.3.0
    ++ added the live/current build to the repository compiled as an *.exe
    ++ preparations for calculations of real time P_rad estimate in W7X VI
       and U+P acquisition
       --> references and local variables, plus display and debugging
    ++ disable structures around all the new stuff for testing
    ++ test VI for voltage output and substructure
       in sequence of trigger event
    ++ found out how the triggering works: FPGA reference from
       AutomatedStartFlow VI inside timer/counter loop

    !!!
        currently stuck, now measurement isn't starting since state of
        calibration is not reached (and beyond)
    !!!

    06/01/2018
    ----------
    v.1.5.1
    ++ updated *.exe's
    ++ nearly finalized the estimation routine, technical part is fine
    ++ performance for 1 -- 10 selected channels is fine (partially) though
       all channels requires up to 3x as much time and hence is not feasible
    ++ index shifting after each ten samples works
    ++ average and P_rad calculation with kbolott and volume
    ++ calibration values of foil properties: R, tau, etc. doesnt seem to
       properly work -- values off the chart and far from reasonable/negative

    AFTER TRIGGER TESTS:
    ++++++++++++++++++++

    ++ channel selection manual stops program from triggering
       blocked at acquiring data
       --> second run though works with manual selection
    ++ standard value of sample rate is 0.0004 ms?!
    ++ repeated Ref1/Ref2 calibration?!
    ++ what happens during SoftReset(3000ms)
    ++ if not shot time published, what happens?

    29/06/2018
    -----------
    v1.8.3
    ++ estimation routine finished (?!) though calculations and voltage output
       to be tested

    !ATTENTION!
        found bug where, when cancelling the routine during acquisition by
        using the stop button of the VI menu bar, the ScanID specifically
        (number of samples acquired previously) is not cleared & reset
        --> the number of samples has to be bigger
            than 10000, since the offset
            acqusition is going up to 10000
        --> this also causes the earlier parts of the routine
            (mainly calibration) to be skipped, since N_samples is always
            bigger than the maximum number of steps in those specific subVI's
        --> hence, device status and calibration values are way off the chart
            or equal to 0 & NaN

            can be 'fixed' by setting the sample number above the current
            'stuck' N_samples and letting the VI run 1-3 times on full with a
            hardware or software trigger from the AutomatedStart.vi
            --> it is essential to letthe routine complete to the fullest
                until the status "Waiting for trigger/idle" is achieved again
    !ATTENTION!

    ++ added/started full P_rad routine right after acquisition

    AFTER 2nd TRIGGER TEST:
    +++++++++++++++++++++++
    ++ upload of data does not happen, however, v1.0.0 does upload properly
       still, either signal step/drop in raw signal or oscillations

    30/08/2018
    -----------
    v2.0.final
    ++ done all the stuff, following description of changes

    STARTING FROM THE TOP LEFT ON THE BLOCKDIAGRAMM:
    ================================================
        --> variable setup/reset at startup of W7X...vi
        --> handover from toplevel AutomatedStart.vi of FPGA reference as
            shift register from previous executions
        --> resetting of FPGA state
        --> setting filter mode to x4D and x3D
        --> xXXB8 mode register hex bits

        SHORT EXCURSION ON  HostFPGAMode.vi:
            ++ possible to set FPGA mode in hex with range of acqusition
               between 80 mV and 10 mV either automatically for all channels,
               or individually
            ++ also hands over the mode register that defines the pins of the
               AD7730 on the board to be used during the mode specified
               by the hex code handed over
            ++ from AD7730 manual p.15, mode register list where B/U has to
               be zero for active, singular polarity acqusition:

            ++ 16 Bit where MD2-0 are the mode settings bits and RN1-0
               specify the pins of the AD
            ++ HIREF has to be 1 for calibration voltage of 5V, 0 otherwise


            MD2/MD1/MD0/BU0/DEN/D1/D0/WL/HREF/ZERO/RN1/RN0/CLKDIS/BO/CH1/CH0
            e.g.: xA0B8 in ex equals to:
                    1010   0000   1011   1000
                    ^^^^          ^ ^^     ^^
                 MD2||||     HIREF| ||  CH1||
                  MD1|||         RN1||   CH0|
                   MD0||          RN0|
                   B/U0|

                MD2-0, BU0     MD2-MD0
                HEX (BIN)       BINARY   STATUS
                ==============================================================
                x8XXX (1000)    1 0 0    Internal Zero-Scale Calibration
                x9XXX (1001)    1 0 0    Internal Zero-Scale Calibration
                xAXXX (1010)    1 0 1    Internal Full-Scale Calibration
                xBXXX (1011)    1 0 1    Internal Full-Scale Calibration
                xCXXX (1100)    1 1 0    System Zero-Scale Calibration
                xDXXX (1101)    1 1 0    System Zero-Scale Calibration
                xEXXX (1110)    1 1 1    System Full-Scale Calibration
                xFXXX (1111)    1 1 1    System Full-Scale Calibration
                x0XXX (0000)    0 0 0    Sync (Idle) Mode Power-On/Reset
                x1XXX (0001)    0 0 0    Sync (Idle) Mode Power-On/Reset
                x2XXX (0010)    0 0 1    Continuous Conversion Mode
                x3XXX (0011)    0 0 1    Continuous Conversion Mode
                x4XXX (0100)    0 1 0    Single Conversion Mode
                x5XXX (0101)    0 1 0    Single Conversion Mode
                x6XXX (0110)    0 1 1    Power-Down (Standby) Mode
                x7XXX (0111)    0 1 1    Power-Down (Standby) Mode

                CH1-0         CH1,CH0
                HEX (BIN)       BIN      POSITIVE IN        NEGATIVE IN
                ==============================================================
                xXXX8 (00)               AIN1(+)            AIN1(-)
                xXXX9 (01)               AIN2(+)            AIN2(-)
                xXXXA (10)               AIN1(-)            AIN1(-)
                xXXXB (11)               AIN1(-)            AIN2(-)

        --> timing mode that calculates epoch time at start so one can use
            that instead of UTC (not working); towards bottom below
            the AC 1.25 kHz referencing
        --> DAC ranges input loading (column of 128)
        --> channel selection file import (column of Nchannels you want)
        --> kbolott and volume file concatenation/import with switch
            for new files/geometries or full channel file (2 columns of 128)

        ++ inside TRUE/FALSE case structure of main routine
            --> synchronises machine/rack mounted FPGAs/ADs
            --> reads offset by internal mechanism on seleted pins
                hostComRegStart.vi
            --> soft reset
            --> populating deviations/means/offset lists
            --> setting up the filter mode with x200, x7D and xXX39
                for calibration values like tau, kappa, R
            --> DMA configuration
            --> actual DAQ filter setup
            --> using input settings to specify acqusition mode
                    ++ with dials and switches to easily change pins and bits
                       default at individual mode, with xXXB8

        --> hostComRegister and waiting until sync and DAQ
        --> starting time measurement outside the DAQ routine
            hReadChannelsUandP.vi
        --> collect references of arrays and single values for voltage output
        --> collect tons of local variables and parameters needed for
            everything inside the acqusition
        --> FPGA reference and two additional clusters!

        ++ BELOW FIND CALCULATION OF POWER FACTORS FROM CALIBRATION VALUES

        ++ inside DAQ routine
            --> unbundling clusters and making local properties

            ++ LOOP OF DAQ
            --> usual timeout and FPGA acqusition procedures, see RawDMA.Read
                for all 128 channels and 1 sample at a time
            --> skipping the first XXXX samples, defined by outside
                located switch on front panel
            --> only after, enter calculations and output routine

            ++ after XXXX exclusion samples
            --> subtract preacquired offsets from raw signal (transformed
                from the int64bit signal given from the RawDMA.Read through
                the specified range bits/scaling bits) and making
                absolute value
            --> filling up live offset generation case selector which is
                beyond sample No. 60 used to correct the signal
            --> Savitzky Golay Filer used to derivate and filter the voltage
                for calculation of P_ch for all 128
                ++ inside SavGol is a PtbyPt FilterFIR method that FIFOs the
                128 channels single sample for N (31...51) points
            --> making the calculation:
                P_ch = F_ch * (tau_ch * dU_ch,filt/dt + tau_fact* U_ch,filt)
            --> concatenating the samples in Nsamples long array afterwards
                (power and voltage)
            --> single channel output reference used with factor (selector
                whether voltage or power)

    ++ real time P_rad estimate
    >> shift sample by one, use real inside for averaging array
    >> fill up the averaging samples for the specified number of channles and
       their index
    >> after that: calc average over each channel, use geometry and factors
       for final calculation of P_rad over the Nchannels used in the av-array
    >> scale for MW
    >> output RT P_rad and av array
    >> finalize execution and output all the arrays

        --> stop time measurement
        --> make all the plots and compare the output stuff with the
            two full P_rad's by the cameras VBC/HBC
        --> make channel status as bool indicators
        --> channel raw and power plots

        --> from internal FPGA timings, make trigger points (epoch time, ns)
            when DAQ started precisely
        --> read trigger from where it was specified (UTC (broken), CODAC,
            internal timing from the start)
        --> stuff 1D arrays and results in to 2D array because no timing
            available for 128 individual properties like RRes etc.
        --> route everythin for upload through, create timing arrays
            tailored specifically for all needs, PARLOGS and DATASTREAMS

        ++ UPLOADS
        >> in general:
           + give label, unit and datatype to 2DData2JSON
           + give dimensionsize (rows) and samplecount (columns) of 2D array
             to 2DDataJSON and dimension of 1 digit/2 digit
           + give data (2D) to the 2DData2JSON and parlog cluster-array
             to W7X1D/2DputQSB
           + full dimensions to be used along 2D sample dimension
             for W7XYYputQSB
           + hand over JSON string buffer from ToJSON to W7XYYputQSB
           + create debugging indicators and HTTP request results
           + QSP parms put under File_PARLOG

    --> finalize execution by handing out the FPGA reference to the waiting
        AutomatedStart.vi

    05/12/2018
    -----------
    v3.1.0 final
    ++ small additions to the final version after user requirements
       and new/understandable filter settings for
    ++ ResetButton function as standalone VI that executes a full reset
    ++ fully overhauled the calibration value routines, since the
       time response
       of the calib execution on the ADC/detector is not on-point
    ++ full power calculation method is afterwards executed to mimick the
       python routine that is used manually to its best performance
    ++ fixed errors in the filter settings, hence timings are now accurate to
       the actual speed acquisition is performed at and the calibration is
       done at the specified 0.4ms mode, not at 0.8ms or higher as the
       sample rate setting specifies

    CALIBRATION ==============================================================
        --> now at 0.4ms time interval so tau is correct
        --> fit is now shifted to the part where, in any case, an actual
            exponential decay occurs in the first calibrational current step
            (after 0.8s) by 50 points or so
        --> for the calculation of kappa the highest current is picked at
            the top of the response, not the fit
        --> using different resistance setup, hence the values of R_sys is
            changed with R_cable and R_load

    PRAD CALCULATION ========================================================
        --> offset subtraction (meanfrom first points or last points
            calculated, depending on whether end is actually plasma off)
        --> if voltage is < 0 at somewhere around 0.05 ms (small mean)
            the voltage has to be flipped
        --> linear fit between value at ON and last sample, then subtract that
            from the signal vector in between
        --> then digital spiking fix (threshold method)
        --> power calculation with geometry, calibration values, filtering and
            averaging
        --> sum of channels

    FILTER SETTINGS/SAMPLE RATE ==============================================
        --> the filter is set with a range of bits in the register of the ADC
        --> you need two entries to the filter register to specify first the
            mode with xYZ which goes to the bits 0/0/SKIP/FAST/0/0/AC/CHOP
        --> second the frequency settings are given to the SF11-SF0 bits
            and then the actual sampling rate can be calculated by a function
            that uses the specified masterclock of the ADC, given a model
            number

            In this case an AD7730 with a master clock frequency of
            f_master = 4.9152 MHz.
            Assuming using the Non-Chop mode, CHOP=0, the DAQ rate is

                f_in = (f_master)/16 * 1/(SF_decimal) ,

            where SF_decimal is the decimal value converted
            from the hexadecimal bits given to the routin (see below).
            In CHOP mode, it becomes

                f_in = (f_master)/16 * 1/(3 * SF_decimal) .

            Hence, the SF_decimal value to use for T_sample in ms is given by

                CHOP:       SF_decimal = (T_sample[ms] * f_master) / (4.8e4)
                Non-CHOP:   SF_decimal = (T_sample[ms] * f_master) / (1.6e3)

        FILTER REGISTER:
            SF11-SF0/ZERO/ZERO/SKIP/FAST/ZERO/ZERO/AC/CHP/DL3/DL2/DL1/DL0
            e.g.: x3D in hex equals to:
                    0011       1110
                    ^^^^       ^^^^
                ZERO||||   ZERO||||
                 ZERO|||    ZERO|||
                  SKIP||       AC||
                   FAST|      CHOP|

                SF11-SF0 (CHOP MODE)
                HEX (BIN) DECIMAL VALUE  FREQUENCY[Hz]  T_sample[ms]
                ===================================================
                x52       82             1250           0.8
                xA4       164            625            1.6
                xCD       205            500            2.0
                x148      328            312            3.2
                x28F      655            156            6.4

    06/07/2019
    -----------
    v3.1.5
    ++ new branch
        QRB_System
    ++ F.Henke added local storage mode
    ++ changed file locations to load to a folder in
        C:\QSB_files\
       since LabVIEW 2014 doesn't take relative paths
    ++ changed default values to be used in laboratory tests

    06/21/2019
    -----------
    v3.1.6
    ++ branch updates on both
    ++ got OG version from after OP1.2b back from torus hall PC since I
       messed up the git upload/version
    ++ some default value changes
    ++ timing tests revealed on the new QRB PC Windows system
        a - heavy load dependence of system for acquisition, since pi cruncher
            exceeded the by LabVIEW used cores load and other
            as well and that changed the output and input both strongly

            http://www.numberworld.org/y-cruncher/ (v.0.7.7 Build 9501)

        b - crash still by memory allocation problems, 150 thousand samples
            not possible, but not all of RAM used?!
        c - skipping feedback doesnt change much of time, roughly 0.02ms
        d - there seems to be a lower limit to the sample time, based off of
            what is set, so you cant go lower than 1.62ms on 1.6ms set, but
            higher is absolutely possible and likely
        e - 0.8ms becomes usable and feasable again with new PC, but is
            but is actually something like 0.83ms
        f - possbile to achieve 19.2ms delay between output and input again,
            roughly as fast as old system (13.8ms before)
        g - there seems to be a great influence of the process priority set
            in windows since it is not a real time based system
        h - LabVIEW setting for multithreading increases performance slightly
            but stops front panel updates until finish


    08/28/2019
    -----------
    v3.2.
    ++ setup for dasens lab work to cross check timing errors
    ++ looking for old filter settings, turns out as

        nC: f_in = (f_master)/16 * 1/(3 * SF_decimal)
        C:  f_in = (f_master)/16 * 1/(SF_decimal)

    N T [ms] HEX (BIN) DECIMAL VALUE FREQUENCY[Hz] T_sample[ms] MODEHEX (BIN)
    ==========================================================================
    0 0.8    x4F       79            1296.2        0.77         3D (nC)
    1 1.6    xA2       162           632.1         1.58         3E (nC)
    2 3.2    x149      329           311.25        3.21         3D (nC)
    3 6.4    x149      328           311.25        3.21         3E (nC)
    4 12.8   x531      1329          77            12.98        3D (nC)
    5 19.2   x7CB      1995          153.98        6.4941       3F (Chop)

    so ... everything almost wrong?!


$ ########################################################################## $

TODOs:
            - measure timing delay in feedback (single channel) as function
              of system load, sample time, sample duration (DAQ time)
            - find 'new' DAQ sample number limit where (without feedback)
              timing gets wrong, see above (v3.1.6)
            - disable spiking fix or make it switchable
            - maybe find new method to start/stop feedback loop,
              since it stops early if sample number is <10000, i.e.
              offset measurement duration

OLD (OP 1.2b):
            - index shifting of the next sample in the acquisition routine
            --> new sample is new last one (No. 10, 11th element)
                and the former i-th sample becomes the (i-1)-th
                since first (1st element) sample is dropped
### DONE!
            --> the 0th sample is the average over all other 10
                hence combined length is 11
### DONE!
            - calculate the average over the 10 samples acquired and
              use the imported kbolott and volume data to estimate a
              P_rad value to pass on to the successfully tested AO voltage
              subqueue
### DONE!
            - disable structures around all selfmade routines and subVIs
### DONE!
            - weighting factors for channels used as estimate
### DONE!
            - time measurement between samples and output voltages
### DONE!
            - make progress bar for overall time passed beyond the T0 trigger
### DONE!
            - change dial from sample rate and number to time covered
### DONE!
            - JSONs and archive upload
### DONE!