# SHIFT28M

[![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/st-tech/zr-shift28m)
![GitHub last commit](https://img.shields.io/github/last-commit/st-tech/zr-shift28m)

The main motivation of the SHIFT28M project is to provide a dataset that contains natural dataset shifts collected from a web service that was actually in operation for several years.
In addition, the SHIFT28M dataset has several types of dataset shifts, allowing us to evaluate the robustness of the model to different types of shifts (e.g., covariate shift and target shift).

We provide the [Datasheet for SHIFT28M](./DATASHEET.md).
This datasheet is based on the [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) [1] template.

| System      | Python 3.6 | Python 3.7 | Python 3.8 |
| :---:              | :---:             | :---:            | :--:              |
| Linux CPU    |  <img src="https://img.shields.io/badge/build-success-brightgreen" /> | <img src="https://img.shields.io/badge/build-success-brightgreen" /> | <img src="https://img.shields.io/badge/build-success-brightgreen" /> |
| Linux GPU    |   <img src="https://img.shields.io/badge/build-success-brightgreen" />  | <img src="https://img.shields.io/badge/build-success-brightgreen" /> | <img src="https://img.shields.io/badge/build-success-brightgreen" /> |
| Windows CPU / GPU | <center>Status Currently Unavailable</center> | <center>Status Currently Unavailable</center> |  <center>Status Currently Unavailable</center> |
| Mac OS CPU|   <img src="https://img.shields.io/badge/build-success-brightgreen" /> |  <img src="https://img.shields.io/badge/build-success-brightgreen" />   |  <img src="https://img.shields.io/badge/build-success-brightgreen" /> |

## Installation

### (WIP) From PyPi

```bash
$ pip install shift28m
```

### From Source

```bash
$ git clone https://github.com/st-tech/zr-shift28m.git
$ cd zr-shift28m
$ poetry build
$ pip install dist/shift28m-xxxx-py3-none-any.whl
```

## Download SHIFT28M dataset

### (WIP) Use Dataset class

You can download SHIFT28M dataset as follows:

```python
from shift28.datasets import NumLikesRegression

dataset = NumLikesRegression(root="./data", download=True)
```

### Download Directly from the Sharable URL

Please access [here](https://drive.google.com/drive/folders/1BExsZkhE5N6Oj_OyFrs2O52WUc0SkZOr?usp=sharing) and download all files.

## Tasks

The following tasks are now available:

| Tasks              | Task type      | Shift type   | # of input dim | # of output dim |
|--------------------|----------------|--------------|----------------|-----------------|
| [NumLikesRegression](https://github.com/st-tech/zr-shift28m/tree/main/benchmarks#regression-for-the-number-of-likes) | regression     | target shift |     (N,25)     | (N,1)           |
| [SumPricesRegression](https://github.com/st-tech/zr-shift28m/tree/main/benchmarks#regression-for-the-sum-of-prices) | regression    | covariate shift, target shift | (N, 1) | (N, 1) |
| ItemPriceRegression| regression     | target shift | (N, H, W)      | (N, 1)          |

## Benchmarks

As templates for numerical experiments on the SHIFT28M dataset, we have published [experimental results for each task with several models](./benchmarks).

## Original Dataset Structure

The original dataset is maintained in jsonl format, and a row consists of the following:

```
{
  "user":{"user_id":"xxxx"},
  "like_num":"xx",
  "set_id":"xxx",
  "items":[
    {"price":"xxxx","item_id":"xxxxxx","category_id1":"xx","category_id2":"xxxxx"},
    ...
  ],
  "publish_date":"yyyy-mm-dd"
}
```



## Contributing
To learn more about making a contribution to SHIFT28M, please see the following materials:
- [Developers Guide](./DEVELOPMENT.md)
- [Task Proposal Guide](./TASK_PROPOSAL.md)
- [Benchmark Proposal Guide](./BENCHMARK.md)

## LICENSE
Please observe the {TBD} license that is listed in this repository.

## Dataset Metadata
The following table is necessary for this dataset to be indexed by search engines such as [Google Dataset Search](https://datasetsearch.research.google.com/).

<div itemscope itemtype="http://schema.org/Dataset">
<table>
  <tr>
    <th>property</th>
    <th>value</th>
  </tr>
  <tr>
    <td>name</td>
    <td><code itemprop="name">SHIFT28M Dataset</code></td>
  </tr>
  <tr>
    <td>alternateName</td>
    <td><code itemprop="alternateName">SHIFT28M</code></td>
  </tr>
  <tr>
    <td>alternateName</td>
    <td><code itemprop="alternateName">shift28m-dataset</code></td>
  </tr>
  <tr>
    <td>url</td>
    <td><code itemprop="url">https://github.com/st-tech/zr-shift28m</code></td>
  </tr>
  <tr>
    <td>sameAs</td>
    <td><code itemprop="sameAs">https://github.com/st-tech/zr-shift28m</code></td>
  </tr>
  <tr>
    <td>description</td>
    <td><code itemprop="description">SHIFT28M is a multi-objective, multi-domain dataset which includes multiple dataset shifts.</code></td>
  </tr>
  <tr>
    <td>provider</td>
    <td>
      <div itemscope itemtype="http://schema.org/Organization" itemprop="provider">
        <table>
          <tr>
            <th>property</th>
            <th>value</th>
          </tr>
          <tr>
            <td>name</td>
            <td><code itemprop="name">ZOZO Research</code></td>
          </tr>
          <tr>
            <td>sameAs</td>
            <td><code itemprop="sameAs">https://ja.wikipedia.org/wiki/ZOZO</code></td>
          </tr>
        </table>
      </div>
    </td>
  </tr>
  <tr>
    <td>license</td>
    <td>
      <div itemscope itemtype="http://schema.org/CreativeWork" itemprop="license">
        <table>
          <tr>
            <th>property</th>
            <th>value</th>
          </tr>
          <tr>
            <td>name</td>
            <td><code itemprop="name">{TBD}</code></td>
          </tr>
          <tr>
            <td>url</td>
            <td><code itemprop="url">{TBD}</code></td>
          </tr>
        </table>
      </div>
    </td>
  </tr>
</table>
</div>

## Citation

```bibtex
@software{https://github.com/st-tech/zr-shift28m,
  url = {https://github.com/st-tech/zr-shift28m},
  author = {Masanari Kimura, Yuki Saito, Kazuya Morishita, Takuma Nakamura, Ryosuke Goto},
  title = {SHIFT28M: Multiobjective Large-Scale Dataset with Distributional Shifts},
  year = {2021},
}
```

## Errata
No errata are currently available.

## References
- [1] Gebru, Timnit, et al. "Datasheets for datasets." arXiv preprint arXiv:1803.09010 (2018).
