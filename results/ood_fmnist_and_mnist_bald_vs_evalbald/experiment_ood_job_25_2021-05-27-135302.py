store = {}
store['timestamp']=1622119982
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=25']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=25
store['worker_id']=25
store['num_workers']=80
store['config']={'seed': 1260, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.7124857902526855})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.032829761505127})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.401484251022339})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.8635988235473633})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 4.130251407623291})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.714449882507324})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5912, 'crossentropy': 3.7043296875}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 56763], ['ood', 49889], ['id', 29088], ['ood', 6612], ['ood', 48437]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.57890300801514, 2.752042349710799, 3.6423470272390865, 4.156418960224942, 4.377789673931452]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.7477805614471436})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.4215450286865234})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.9000139236450195})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.919684648513794})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.9323174953460693})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.096201181411743})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.215646743774414})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.2274508476257324})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.5857954025268555})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.4038901329040527})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.9458532333374023})
store['active_learning_steps'][1]['training']['best_epoch']=8
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5907, 'crossentropy': 3.427681640625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 56561], ['id', 35776], ['id', 14431], ['id', 18105], ['id', 42858]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0150899101871123, 1.8960951362636345, 2.65730433955852, 3.2666064799004877, 3.7187773234557344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.749446153640747})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.5229101181030273})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.695639133453369})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.57773494720459})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.477450370788574})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.5083112716674805})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6041, 'crossentropy': 2.88602578125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 33574], ['id', 41429], ['id', 26636], ['id', 48804], ['id', 46434]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0787628044847035, 2.021241406542785, 2.7713914481172557, 3.3438923798565723, 3.7436822943793446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.569045901298523})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.12979793548584})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.336116075515747})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4073057174682617})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.4980275630950928})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3533177375793457})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.592818260192871})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.9203901290893555})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.078019380569458})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6534, 'crossentropy': 2.4873115234375}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 58300], ['id', 54017], ['ood', 33227], ['id', 17744], ['id', 57611]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0344956233197369, 1.90981256592302, 2.6391866455838215, 3.221321559390587, 3.67190145997865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3353886604309082})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.461166501045227})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.727752447128296})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.9691965579986572})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.170088291168213})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.093986988067627})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.2312912940979004})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.198482036590576})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.391268730163574})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.200913190841675})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.217761516571045})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.345797061920166})
store['active_learning_steps'][4]['training']['best_epoch']=9
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6767, 'crossentropy': 2.6103453125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 42192], ['id', 59760], ['id', 49167], ['ood', 26241], ['ood', 39510]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.8971805777658726, 1.7715958133211673, 2.561096721022178, 3.214187748365905, 3.657892179954194]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3475757837295532})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.7308764457702637})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.107332229614258})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.031738758087158})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.303560733795166})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.3050780296325684})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.529290199279785})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6563, 'crossentropy': 2.1722380859375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 20740], ['id', 39279], ['id', 5445], ['id', 7755], ['id', 16530]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.8804124717406232, 1.6650487347002279, 2.3346780030640097, 2.9134928379952933, 3.374051396181615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.32527494430542})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.5507395267486572})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.1052050590515137})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.059201240539551})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.246307849884033})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6324, 'crossentropy': 1.7543603515625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 11549], ['id', 31612], ['id', 28663], ['id', 2731], ['id', 36306]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8028526573075923, 1.454497375131528, 2.0394090852426956, 2.5506231520828404, 2.987561803704237]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2745718955993652})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.5319651365280151})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.71122145652771})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.8550143241882324})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.9159353971481323})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.088252067565918})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.666, 'crossentropy': 1.8282744140625}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 38016], ['id', 25382], ['id', 59105], ['ood', 56244], ['id', 42507]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8908661807180769, 1.6927726022184992, 2.3534985576798624, 2.9240292204592997, 3.36984347505774]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2058606147766113})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.417593240737915})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.633302927017212})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.8559761047363281})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.8084967136383057})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.9296540021896362})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.0382609367370605})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.075138807296753})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.186398506164551})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.328810214996338})
store['active_learning_steps'][8]['training']['best_epoch']=7
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6667, 'crossentropy': 2.202248046875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 4267], ['id', 31662], ['id', 54101], ['id', 49152], ['id', 28962]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.9602693052619631, 1.8831882548075636, 2.659343373927621, 3.2487978996560756, 3.6878490518004616]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.1665514707565308})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2612104415893555})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.5781009197235107})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.776371717453003})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.8745145797729492})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.200833320617676})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.1874513626098633})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.4412081241607666})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6567, 'crossentropy': 2.0714548828125}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 6832], ['id', 52991], ['id', 43542], ['id', 55157], ['id', 8689]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8970306711807476, 1.7217366506025025, 2.4654170282277734, 3.0686651268980025, 3.5255693586706833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2340645790100098})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.3479053974151611})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.5014829635620117})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.5901110172271729})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.7914209365844727})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.782576322555542})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.7696928977966309})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6684, 'crossentropy': 1.70504609375}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 39545], ['id', 44630], ['id', 25184], ['id', 25105], ['id', 31654]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.925779769391045, 1.7921138220940032, 2.5453115879970536, 3.1851874900138952, 3.6573631778237736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.2577495574951172})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2536990642547607})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.4101879596710205})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.7041738033294678})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.4513369798660278})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.8051475286483765})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.8480727672576904})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.9925580024719238})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.9643057584762573})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.0545010566711426})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.9851019382476807})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.032658100128174})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.129312515258789})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.3220834732055664})
store['active_learning_steps'][11]['training']['best_epoch']=11
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6722, 'crossentropy': 2.2421796875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 56978], ['id', 32592], ['id', 35668], ['id', 16965], ['id', 38613]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9399701044125195, 1.8171167194143711, 2.5860238993820133, 3.212985718161667, 3.6732378293591603]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.2930536270141602})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.136920690536499})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.3119750022888184})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.4521623849868774})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.5275306701660156})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.756615400314331})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.607576608657837})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.8308594226837158})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.9140599966049194})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.9587953090667725})
store['active_learning_steps'][12]['training']['best_epoch']=7
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7064, 'crossentropy': 1.7189322265625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 51163], ['id', 36424], ['id', 31717], ['ood', 44939], ['id', 7671]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.868863483111747, 1.6955258911439874, 2.4346496760025094, 3.0630230292345253, 3.556399022223868]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2159841060638428})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1176834106445312})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.3369166851043701})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.4408633708953857})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.4536919593811035})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.7196320295333862})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.652148723602295})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.7902512550354004})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6985, 'crossentropy': 1.55070380859375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 48019], ['id', 33781], ['id', 1120], ['id', 20009], ['id', 47079]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7751843472257849, 1.519230298184346, 2.2172078230008747, 2.804604153565294, 3.2652641496763266]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.270857334136963})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1300835609436035})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.3182604312896729})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.3434553146362305})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.5273702144622803})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.5694248676300049})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.7036161422729492})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.7567710876464844})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7145, 'crossentropy': 1.5027185546875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 3405], ['id', 29755], ['id', 13565], ['id', 1381], ['id', 54813]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8370651311756401, 1.593935270657803, 2.264251481195471, 2.826124296086853, 3.28960610947842]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2828264236450195})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1865782737731934})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1435989141464233})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.4063209295272827})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.4446430206298828})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.4658410549163818})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.7054178714752197})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.6129213571548462})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.5816307067871094})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.5943330526351929})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.7796616554260254})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7712185382843018})
store['active_learning_steps'][15]['training']['best_epoch']=9
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7172, 'crossentropy': 1.6787244140625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 57225], ['id', 18530], ['id', 40549], ['id', 7595], ['id', 20302]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9645803805778026, 1.8308950545974758, 2.593671706920926, 3.221678047455688, 3.6849929265275563]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.2729501724243164})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1026360988616943})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1915597915649414})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.321530818939209})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.397522211074829})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.555577278137207})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.5564162731170654})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.6822956800460815})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.6886067390441895})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.6683313846588135})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.7959519624710083})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.856858491897583})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.8891534805297852})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.8795065879821777})
store['active_learning_steps'][16]['training']['best_epoch']=11
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7306, 'crossentropy': 1.8784751953125}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 3731], ['id', 13903], ['id', 19138], ['id', 36765], ['id', 6977]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.046282301565616, 1.9902981347642004, 2.812790333134086, 3.3972999666178563, 3.8459170339903705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.2779268026351929})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1467968225479126})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1816575527191162})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.34423828125})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.3546955585479736})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.4300482273101807})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.6441521644592285})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.5470314025878906})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7113, 'crossentropy': 1.44458583984375}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 7298], ['id', 15716], ['id', 35231], ['id', 12994], ['id', 38806]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8221743223822551, 1.599858047379569, 2.282822601699836, 2.872079437311447, 3.3471333114065107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2711610794067383})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.24967360496521})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2467344999313354})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3944039344787598})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.5637614727020264})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.6842103004455566})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.8790676593780518})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.802163004875183})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.7448418140411377})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6959, 'crossentropy': 1.7165765625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 28940], ['id', 41893], ['id', 49078], ['id', 56948], ['id', 13384]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8597608608041032, 1.6125556093078526, 2.311840092508321, 2.9215586009178542, 3.3960238352386884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.263062834739685})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0890684127807617})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.2338844537734985})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.3709455728530884})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.6583786010742188})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.5008184909820557})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.8074615001678467})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.5854198932647705})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.7383666038513184})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.0214972496032715})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.8857758045196533})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7218, 'crossentropy': 1.7163236328125}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 58238], ['id', 36416], ['id', 29376], ['id', 46619], ['id', 4148]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.9118331610642285, 1.7050351422235677, 2.4317631487352624, 3.0325310421349805, 3.48148984262086]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2657548189163208})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1301560401916504})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1957309246063232})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.2860617637634277})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.3466360569000244})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.436493158340454})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.6609563827514648})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.603214979171753})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.7255373001098633})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.7828865051269531})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.8653110265731812})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7176, 'crossentropy': 1.6841755859375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 55098], ['id', 49559], ['id', 18255], ['ood', 16676], ['id', 36]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8771415226640269, 1.6382099290544558, 2.327860555579883, 2.9050073268474836, 3.372404075856913]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2637189626693726})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.13985276222229})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1700780391693115})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.2633838653564453})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.4137182235717773})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.5639684200286865})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.6100819110870361})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.550827980041504})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.6853621006011963})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.692457914352417})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.9675970077514648})
store['active_learning_steps'][21]['training']['best_epoch']=8
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7087, 'crossentropy': 1.61801796875}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 32727], ['id', 32838], ['id', 20650], ['id', 27096], ['id', 30850]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7795911407914273, 1.5093124797996653, 2.1807762381101234, 2.7712999064898547, 3.255860394898252]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.291229248046875})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0689899921417236})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1317801475524902})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.2622863054275513})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.3316731452941895})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4549285173416138})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.5478318929672241})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.6615456342697144})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.6613104343414307})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.4905009269714355})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.6277308464050293})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.6933743953704834})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.5769623517990112})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.9164543151855469})
store['active_learning_steps'][22]['training']['best_epoch']=11
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7202, 'crossentropy': 1.77575078125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 27479], ['id', 59741], ['id', 8485], ['ood', 20581], ['id', 1473]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9632979413451974, 1.8272654034025386, 2.580844217736411, 3.1921655771252198, 3.6493094549898792]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.3391847610473633})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.101076602935791})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.1444246768951416})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.263911247253418})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.3069801330566406})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.5210742950439453})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.6008628606796265})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.6554076671600342})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7142, 'crossentropy': 1.41985517578125}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 19044], ['id', 12692], ['ood', 49500], ['id', 31627], ['id', 52635]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7624454312137703, 1.4759902011925417, 2.1141280194461123, 2.6660117439801407, 3.1307338878994653]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.325089693069458})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1012983322143555})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2250800132751465})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1852774620056152})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.4051588773727417})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.492978811264038})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.5668584108352661})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.6632330417633057})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.7768274545669556})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.7523908615112305})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.782562494277954})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.6246148347854614})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.8865208625793457})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.2218847274780273})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.8887059688568115})
store['active_learning_steps'][24]['training']['best_epoch']=12
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.7161, 'crossentropy': 1.6801927734375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 31256], ['id', 47664], ['id', 55765], ['id', 7667], ['id', 7101]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.916482654902683, 1.7575805533206532, 2.4700397519485486, 3.0466478318274195, 3.5060375991924655]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.480595350265503})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1540281772613525})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1800352334976196})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.3027470111846924})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.5147902965545654})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.4850044250488281})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.6212165355682373})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7744543552398682})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.712930679321289})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6982, 'crossentropy': 1.58940400390625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 24815], ['id', 45176], ['id', 18379], ['id', 9924], ['id', 20982]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7237323783196823, 1.4139903270835155, 2.025577271483048, 2.557666757356655, 3.013361679449238]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3399596214294434})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0799154043197632})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0726146697998047})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.2578163146972656})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.3846828937530518})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.3615155220031738})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.3976515531539917})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6134902238845825})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.4804208278656006})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.6549501419067383})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.745052695274353})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.787276268005371})
store['active_learning_steps'][26]['training']['best_epoch']=9
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7182, 'crossentropy': 1.6725931640625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 45510], ['id', 50529], ['id', 5346], ['id', 49763], ['ood', 29723]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9604216685737161, 1.7855719826123977, 2.517588939834029, 3.1322460137474017, 3.593983159737382]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.4371075630187988})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1812207698822021})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1751600503921509})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.3051944971084595})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.4935591220855713})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.5385806560516357})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.4573533535003662})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.9142000675201416})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7237262725830078})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.5829509496688843})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.2107200622558594})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.7713501453399658})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.834496259689331})
store['active_learning_steps'][27]['training']['best_epoch']=10
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7128, 'crossentropy': 1.8386767578125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 39750], ['id', 34122], ['id', 372], ['id', 28097], ['id', 47927]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9582488612698954, 1.8192076523195153, 2.5938541364938583, 3.2084980013384925, 3.6438676531871774]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.3994908332824707})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1403319835662842})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1165482997894287})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2136445045471191})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2843029499053955})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.3981705904006958})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.537286400794983})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.4812617301940918})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.5586460828781128})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.7393680810928345})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.782515287399292})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7127, 'crossentropy': 1.5690203125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 16490], ['id', 25851], ['id', 21810], ['id', 38275], ['id', 54969]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0248896535989829, 1.7881467398087745, 2.478769260237266, 3.049868763368478, 3.4769902483167474]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.48828125, 'crossentropy': 1.5223758220672607})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1159546375274658})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0858314037322998})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.101011037826538})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.233953833580017})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.2817449569702148})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.348808765411377})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.4276630878448486})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.5372529029846191})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.4828109741210938})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.6722970008850098})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.4750568866729736})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.7786455154418945})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.719315767288208})
store['active_learning_steps'][29]['training']['best_epoch']=11
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7124, 'crossentropy': 1.8029046875}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 9692], ['id', 9862], ['id', 11901], ['id', 28821], ['id', 27995]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8814492880471048, 1.6818152523740735, 2.389183677052751, 2.963607493746263, 3.4303389704559457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.4552090167999268})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.122929573059082})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1103451251983643})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.2301585674285889})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.2882860898971558})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.3745040893554688})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.5247114896774292})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.4512165784835815})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7187, 'crossentropy': 1.27330517578125}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 70], ['id', 6000], ['id', 30218], ['id', 11150], ['id', 30553]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6830884699141715, 1.3281493454333209, 1.929752654973404, 2.474914580516465, 2.938144947603626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.439462661743164})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.117405652999878})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1073112487792969})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1913464069366455})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.1926758289337158})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.2859727144241333})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.3213279247283936})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.344417929649353})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.4206606149673462})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.5086696147918701})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.4975476264953613})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.5395143032073975})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.6222938299179077})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.6619899272918701})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.683867335319519})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.7879345417022705})
store['active_learning_steps'][31]['training']['best_epoch']=13
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.729, 'crossentropy': 1.721745703125}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 4915], ['id', 57392], ['id', 2067], ['id', 17565], ['id', 32065]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.1034897677735924, 2.0090786848399658, 2.699743627525006, 3.2637563636584197, 3.6936571358796293]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.4423785209655762})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1407796144485474})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.070112705230713})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1594452857971191})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.2787704467773438})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.283340334892273})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.5039904117584229})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6978, 'crossentropy': 1.1776439453125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 58328], ['id', 8449], ['id', 18292], ['id', 29437], ['id', 11651]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6032923100968706, 1.1893342855415723, 1.7184337432257628, 2.2002826730434952, 2.615329051899554]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5068359375, 'crossentropy': 1.5339775085449219})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1856164932250977})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1520397663116455})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.2495341300964355})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.2927579879760742})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.271601915359497})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.3705023527145386})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.4783152341842651})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.3775633573532104})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.5270822048187256})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.6652655601501465})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.6212162971496582})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.7572118043899536})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.7067996263504028})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.801185131072998})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.8484675884246826})
store['active_learning_steps'][33]['training']['best_epoch']=13
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7204, 'crossentropy': 1.8198201171875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 54123], ['id', 24141], ['id', 49864], ['id', 3301], ['id', 52509]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9735690620197779, 1.8617545623100535, 2.625273735089465, 3.25766033004758, 3.732392651090888]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.4822897911071777})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1307176351547241})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1655642986297607})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1828794479370117})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.2520649433135986})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.3021435737609863})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.4643874168395996})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.5424606800079346})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.4699174165725708})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.5738872289657593})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.8114020824432373})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.6500179767608643})
store['active_learning_steps'][34]['training']['best_epoch']=9
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6913, 'crossentropy': 1.62745537109375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 36293], ['id', 57976], ['id', 9771], ['id', 5413], ['id', 29281]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8066215978651667, 1.5954753091838265, 2.318019127898099, 2.9239934732291033, 3.3956841734880854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.525390625, 'crossentropy': 1.491858720779419})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1420645713806152})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1608229875564575})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1937992572784424})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.26785409450531})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3117460012435913})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.553124189376831})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.4611420631408691})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.700669527053833})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.6631159782409668})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.7371790409088135})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7381558418273926})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.7994325160980225})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.6974773406982422})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.7513999938964844})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.7164021730422974})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.6492104530334473})
store['active_learning_steps'][35]['training']['best_epoch']=14
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7026, 'crossentropy': 1.91507421875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 32498], ['id', 59264], ['id', 49496], ['id', 56635], ['id', 20624]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9810862982352431, 1.8782575236000207, 2.6520969101585337, 3.2894904314862607, 3.765230348594942]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.50390625, 'crossentropy': 1.605155348777771})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.210672378540039})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1006585359573364})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1451218128204346})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1687960624694824})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.2782856225967407})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.371692180633545})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.5021169185638428})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.619659662246704})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.5952816009521484})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.4971883296966553})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.6307373046875})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7729814052581787})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.8235132694244385})
store['active_learning_steps'][36]['training']['best_epoch']=11
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7152, 'crossentropy': 1.61113125}
