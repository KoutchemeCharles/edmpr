# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""CodeBLEU metric."""

import evaluate
import datasets

#these were added to fix evaluate load of dependencies
from .bleu import corpus_bleu
from .utils import pad_sequence
from .weighted_ngram_match import ngrams
from .syntax_match import calc_syntax_match
from .parser_DFG import DFG_python
from .parser_utils import tree_to_token_index
from .dataflow_match import calc_dataflow_match

from .my_codebleu import calc_codebleu


# TODO: Add BibTeX citation
_CITATION = """\
@InProceedings{huggingface:module,
title = {CodeBLEU: A Metric for Evaluating Code Generation},
authors={Sedykh, Ivan},
year={2022}
}
"""

# TODO: Add description of the module here
_DESCRIPTION = """\
This new module is an adaptation of the original CodeBLEU metric from CodexGLUE benchmark 
for evaluating code generation.
"""


# TODO: Add description of the arguments of the module here
_KWARGS_DESCRIPTION = """
Calculates how good are predictions given some references, using certain scores
Args:
    predictions: list of predictions to score. Each predictions
        should be a string with tokens separated by spaces.
    references: list of lists of references. Each list 
        should contain len(predictions) items.
    lang: programming language in ['java','js','c_sharp','php','go','python','ruby']
    tokenizer: tokenizer function str -> List[str], Defaults to lambda s: s.split()
    params: str, weights for averaging(see CodeBLEU paper). 
        Defaults to equal weights "0.25,0.25,0.25,0.25".
Returns:
    CodeBLEU: resulting score,
    ngram_match_score: See paper CodeBLEU,
    weighted_ngram_match_score: See paper CodeBLEU,
    syntax_match_score: See paper CodeBLEU,
    dataflow_match_score: See paper CodeBLEU,
Examples:

    >>> codebleu = evaluate.load("my_new_module")
    >>> results = my_new_module.compute(references=[0, 1], predictions=[0, 1])
    >>> print(results)
    {'accuracy': 1.0}
"""

# TODO: Define external resources urls if needed
# BAD_WORDS_URL = "http://url/to/external/resource/bad_words.txt"


@evaluate.utils.file_utils.add_start_docstrings(_DESCRIPTION, _KWARGS_DESCRIPTION)
class codebleu(evaluate.Metric):
    """CodeBLEU metric from CodexGLUE"""

    def _info(self):
        return evaluate.MetricInfo(
            description=_DESCRIPTION,
            citation=_CITATION,
            inputs_description=_KWARGS_DESCRIPTION,
            features=[
                datasets.Features(
                    {
                        "predictions": datasets.Value("string", id="sequence"),
                        "references": datasets.Sequence(datasets.Value("string", id="sequence"), id="references"),
                    }
                ),
                datasets.Features(
                    {
                        "predictions": datasets.Value("string", id="sequence"),
                        "references": datasets.Value("string", id="sequence"),
                    }
                ),                
            ],
            reference_urls=[
                "https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/code-to-code-trans/evaluator",
                "https://arxiv.org/abs/2009.10297",
            ],
        )

    def _download_and_prepare(self, dl_manager):
        """Optional: download external resources useful to compute the scores"""
        # TODO: Download external resources if needed
        # source CodeBLEU/parser/build.sh
        # print(dl_manager)
        self.kw_dir = dl_manager.download_and_extract("https://huggingface.co/spaces/dvitel/codebleu/resolve/main/keywords.tar.gz")
        print("Downloaded keywords to", self.kw_dir)
        self.langso_dir = dl_manager.download("https://huggingface.co/spaces/dvitel/codebleu/resolve/main/my-languages.so")
        print("Downloaded languages.so to", self.langso_dir)

    def _compute(self, predictions, references, lang = "python", tokenizer=None, params="0.25,0.25,0.25,0.25"):
        """Returns the scores"""
        res = calc_codebleu(
            predictions=predictions,
            references=references,
            lang=lang,
            tokenizer=tokenizer,
            params=params,
            kw_dir = self.kw_dir,
            langso_dir = self.langso_dir
        )
        return res
