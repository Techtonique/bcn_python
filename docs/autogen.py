# -*- coding: utf-8 -*-
import pathlib
import keras_autodoc

PAGES = {    
    'documentation/classifier.md': [
        'BCN.BCNClassifier.BCNClassifier',
        'BCN.BCNClassifier.BCNClassifier.fit',
        'BCN.BCNClassifier.BCNClassifier.predict',
        'BCN.BCNClassifier.BCNClassifier.predict_proba',
    ],
    'documentation/regressor.md': [
       'BCN.BCNRegressor.BCNRegressor',
       'BCN.BCNRegressor.BCNRegressor.fit',
       'BCN.BCNRegressor.BCNRegressor.predict',
    ]
}

bcn_dir = pathlib.Path(__file__).resolve().parents[1]


def generate(dest_dir):
    template_dir = bcn_dir / 'docs' / 'templates'

    doc_generator = keras_autodoc.DocumentationGenerator(
        PAGES,
        'https://github.com/Techtonique/bcn_python/blob/main',
        template_dir,
    )
    doc_generator.generate(dest_dir)
    
if __name__ == '__main__':
    generate(bcn_dir / 'docs' / 'sources')