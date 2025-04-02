# Robust directional analysis of magnetic microscopy images using non-linear inversion and iterative Euler deconvolution

by
[Gelson F. Souza-Junior](https://orcid.org/0000-0002-5695-4239),
[Leonardo Uieda](https://orcid.org/0000-0001-6123-9515),
[Ricardo I. F. Trindade](https://orcid.org/0000-0001-9848-9550),
[Roger R. Fu](https://orcid.org/0000-0003-3635-2676),
[Ualisson D. Bellon](https://orcid.org/0000-0002-4599-6548),
[Yago M. Castro](https://orcid.org/0009-0003-3884-9675).

This repository contains the data and source code used to produce the results
presented in:

> Souza-Junior, G. F., Uieda, L., Trindade, R. I. F., Fu, R. R., Bellon, U. D.,
> and Castro, Y. M. (2025). Robust directional analysis of magnetic microscopy
> images using non-linear inversion and iterative Euler deconvolution.
> EarthArXiv. doi:[10.31223/X5N42F](https://doi.org/10.31223/X5N42F)

|  | Info |
|-:|:-----|
| Version of record | https://doi.org/JOURNAL_DOI |
| Open-access preprint on EarthArXiv | https://doi.org/10.31223/X5N42F |
| Archive of this repository | https://doi.org/10.6084/m9.figshare.28560872 |
| Reproducing our results | [`REPRODUCING.md`](REPRODUCING.md) |

## Abstract

Scientists often study entire samples to understand their overall properties,
but this approach can miss important details. To get a clearer picture,
researchers are improving methods that focus on smaller regions of a sample. In
paleomagnetism, a field that studies the Earth's ancient magnetic field,
magnetic microscopy allows scientists to examine tiny areas with high
precision. In this study, we use magnetic microscopy data to determine the
direction of magnetization in samples. To do this, we apply a mathematical
method called Euler deconvolution, which helps solve complex calculations and
reduce uncertainty. We also refine our results with an additional step that
improves accuracy and removes unwanted signals. We tested this approach on both
simulated and real data. Our results show that this new method can detect
weaker magnetic sources and accurately determine the direction of
magnetization. When applied to real samples, it successfully identified their
original magnetic direction. This represents an important step in using
magnetic microscopy for paleomagnetic research.

## License

All Python source code (including `.py` and `.ipynb` files) is made available
under the MIT license. You can freely use and modify the code, without
warranty, so long as you provide attribution to the authors. See
`LICENSE-MIT.txt` for the full license text.

The manuscript text (including all LaTeX files), figures, and data/models
produced as part of this research are available under the [Creative Commons
Attribution 4.0 License (CC-BY)][cc-by]. See `LICENSE-CC-BY.txt` for the full
license text.

[cc-by]: https://creativecommons.org/licenses/by/4.0/
