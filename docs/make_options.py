from BPt.helpers.ML_Helpers import get_objects_by_type, get_objects
from BPt.pipeline.Scorers import get_scorers_by_type

from BPt.pipeline.Scorers import AVALIABLE as AVALIABLE_SCORERS
from BPt.pipeline.Scorers import SCORERS

from BPt.pipeline.Models import AVALIABLE as AVALIABLE_MODELS
from BPt.pipeline.Models import MODELS

from BPt.pipeline.Loaders import LOADERS
from BPt.pipeline.Transformers import TRANSFORMERS
from BPt.pipeline.Scalers import SCALERS
from BPt.pipeline.Imputers import IMPUTERS

from BPt.pipeline.Feature_Selectors import AVALIABLE as AVALIABLE_SELECTORS
from BPt.pipeline.Feature_Selectors import SELECTORS

from BPt.pipeline.Ensembles import AVALIABLE as AVALIABLE_ENSEMBLES
from BPt.pipeline.Ensembles import ENSEMBLES

from BPt.default.default_params import PARAMS
from BPt.helpers.Docstring_Helpers import get_name, get_scorer_name


def main_category(lines, name):

    lines.append('.. _' + name + ':')
    lines.append(' ')

    stars = ''.join('*' for i in range(len(name)))
    lines.append(stars)
    lines.append(name)
    lines.append(stars)

    lines.append('')

    return lines


def add_block(lines, problem_types, AVALIABLE=None, OBJS=None):
    '''If AVALIABLE and OBJS stay none, assume that showing scorers'''

    for pt in problem_types:
        lines.append(pt)
        lines.append(''.join('=' for i in range(len(pt))))

        if AVALIABLE is None and OBJS is None:
            objs = get_scorers_by_type(pt)
            scorer = True

        else:
            objs = get_objects_by_type(pt, AVALIABLE, OBJS)
            scorer = False

        for obj in objs:
            lines = add_obj(lines, obj, scorer=scorer)

        lines.append('')

    return lines


def add_no_type_block(lines, OBJS):

    lines.append('All Problem Types')
    lines.append('=================')

    objs = get_objects(OBJS)

    for obj in objs:
        lines = add_obj(lines, obj, scorer=False)

    lines.append('')
    return lines


def add_obj(lines, obj, scorer=False):
    '''Obj as (obj_str, obj, obj_params),
    or if scorer = True, can have just
    obj_str and obj.'''

    obj_str = '"' + obj[0] + '"'
    lines.append(obj_str)
    lines.append(''.join(['*' for i in range(len(obj_str))]))
    lines.append('')

    if scorer:
        o_path = get_scorer_name(obj[1])
        lines.append('  Base Func Documenation: :func:`' + o_path + '`')
    else:
        o_path = get_name(obj[1])
        lines.append('  Base Class Documenation: :class:`' + o_path + '`')
        lines = add_params(lines, obj[2])

    lines.append('')
    return lines


def add_params(lines, obj_params):

    lines.append('')
    lines.append('  Param Distributions')
    lines.append('')

    for p in range(len(obj_params)):

        # Get name
        params_name = obj_params[p]
        lines.append('\t' + str(p) + '. "' + params_name + '" ::')
        lines.append('')

        # Show info on the params
        params = PARAMS[params_name]
        if len(params) > 0:
            lines = add_param(lines, params)
        else:
            lines.append('\t\tdefaults only')

        lines.append('')

    return lines


def add_param(lines, params):

    for key in params:

        line = '\t\t' + key + ': '
        value = params[key]
        line += repr(value)
        lines.append(line)

    return lines


problem_types = ['binary', 'regression', 'categorical']

lines = []

lines = main_category(lines, 'Models')
lines.append('Different base obj choices for the :class:`Model<BPt.Model>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('The avaliable models are further broken down by which can work' +
             'with different problem_types.')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('')
lines = add_block(lines, problem_types, AVALIABLE_MODELS, MODELS)

lines = main_category(lines, 'Scorers')

lines.append('Different availible choices for the `scorer` parameter' +
             ' are shown below.')
lines.append('`scorer` is accepted by ' +
             ':class:`Problem_Spec<BPt.Problem_Spec>` and ' +
             ':class:`Param_Search<BPt.Param_Search>`.')
lines.append('The str indicator for each `scorer` is represented by' +
             'the sub-heading (within "")')
lines.append('The avaliable scorers are further broken down by which can' +
             ' work with different problem_types.')
lines.append('Additionally, a link to the original models documentation ' +
             'is shown.')
lines.append('')

lines = add_block(lines, problem_types)


lines = main_category(lines, 'Loaders')
lines.append('Different base obj choices for the :class:`Loader<BPt.Loader>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('')
lines = add_no_type_block(lines, LOADERS)


lines = main_category(lines, 'Imputers')
lines.append('Different base obj choices for the :class:`Imputer<BPt.Imputer>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('Note that if the iterative imputer is requested, base_model must also be passed.')
lines.append('')
lines = add_no_type_block(lines, IMPUTERS)


lines = main_category(lines, 'Scalers')
lines.append('Different base obj choices for the :class:`Scaler<BPt.Scaler>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('')
lines = add_no_type_block(lines, SCALERS)


lines = main_category(lines, 'Transformers')
lines.append('Different base obj choices for the :class:`Transformer<BPt.Transformer>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('')
lines = add_no_type_block(lines, TRANSFORMERS)


# lines = main_category(lines, 'Samplers')
# lines.append('Different base obj choices for the :class:`Sampler<BPt.Sampler>` are shown below')
# lines.append('The exact str indicator, as passed to the `obj` param is represented' +
#             ' by the sub-heading (within "")')
# lines.append('Additionally, a link to the original models documentation ' +
#             'as well as the implemented parameter distributions are shown.')
# lines.append('')
# lines = add_no_type_block(lines, SAMPLERS)


lines = main_category(lines, 'Feat Selectors')
lines.append('Different base obj choices for the :class:`Feat_Selector<BPt.Feat_Selector>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('The avaliable feat selectors are further broken down by which can work' +
             'with different problem_types.')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('')
lines = add_block(lines, problem_types, AVALIABLE_SELECTORS, SELECTORS)


lines = main_category(lines, 'Ensemble Types')
lines.append('Different base obj choices for the :class:`Ensemble<BPt.Ensemble>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('The avaliable ensembles are further broken down by ' +
             'which can work' +
             'with different problem_types.')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('Also note that ensemble require a few extra params! I.e., in general, all DESlib based ensemble need needs_split = True')
lines.append('')
lines = add_block(lines, problem_types, AVALIABLE_ENSEMBLES, ENSEMBLES)


with open('options.rst', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')


