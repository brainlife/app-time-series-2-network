[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-brainlife.app.372-blue.svg)](https://doi.org/10.25663/brainlife.app.372)

# app-time-series-2-network
Converts an NxT time series to an NxN functional connectivity matrix, where N is the number of nodes and T is the number of time points. Such a functional connectivity matrix can be submitted to functional brain network analyses. 

### Authors 

- Josh Faskowitz (joshua.faskowitz@gmail.com) 

### Funding 

[![NSF-GRFP-1342962](https://img.shields.io/badge/NSF_GRFP-1342962-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1342962)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations 

Please cite the following articles when publishing papers that used data, code or other resources created by the brainlife.io community. 

Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). https://doi.org/10.1038/s41597-019-0073-y

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
        "timeseries": "/path/timeseries.h5",
        "discard": "4",
        "similaritymeas" "correlation"
}
```

The `timeseries` provided is the most important file. This is an `h5` file that can be made with the bold-2-timeseries app: https://doi.org/10.25663/brainlife.app.369. The `discard` option is for the number of frames at the beginning of the bold.nii.gz to cutoff. The `similaritmeas` is the similarity measure type, which can be `correlation`, `partialcorrelation`, or `covariance`. Mainly, you'll want to use simple `correlation`.

3. Launch the App by executing `main`

```bash
./main
```

## Output

All output files will be generated under the current working directory (pwd), in directories called `output_network`. Specifically, a conmat datatype object will be made, which will contain a csv of the desired connectivity matrix. 

### Dependencies

This App uses [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you can run this script in a unix enviroment with:  

  - python3: https://www.python.org/downloads/
  - jq: https://stedolan.github.io/jq/
  
  #### MIT Copyright (c) Josh Faskowitz & brainlife.io

<sub> This material is based upon work supported by the National Science Foundation Graduate Research Fellowship under Grant No. 1342962. Any opinion, findings, and conclusions or recommendations expressed in this material are those of the authors(s) and do not necessarily reflect the views of the National Science Foundation. </sub>
