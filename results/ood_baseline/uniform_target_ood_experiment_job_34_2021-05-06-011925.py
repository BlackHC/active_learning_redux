store = {}
store['timestamp']=1620260365
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=34']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=34
store['worker_id']=34
store['num_workers']=40
store['config']={'seed': 48, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.3060903549194336})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.823085308074951})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.9566354751586914})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9516611099243164})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6789, 'crossentropy': 1.99866796875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 49150], ['ood', 40031], ['ood', 28943], ['ood', 30332], ['ood', 7212]], 'labels': [0, 1, 3, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.5753858089447021})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.6603025197982788})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.8642326593399048})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.061239242553711})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.706, 'crossentropy': 1.39905947265625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 51549], ['ood', 58245], ['ood', 52910], ['id', 29901], ['id', 25013]], 'labels': [4, 1, 5, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.4126479625701904})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.60127592086792})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.9227867126464844})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.9658417701721191})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7255, 'crossentropy': 1.30863525390625}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 43414], ['id', 58441], ['ood', 26483], ['ood', 15163], ['id', 18714]], 'labels': [7, 2, 7, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.45098876953125})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.7260380983352661})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.7541019916534424})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.7591071128845215})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7238, 'crossentropy': 1.2591375}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 25772], ['ood', 5150], ['id', 57530], ['ood', 3178], ['id', 22564]], 'labels': [6, 2, 4, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.328209638595581})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.4752449989318848})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.6223849058151245})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.6660895347595215})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7224, 'crossentropy': 1.24370087890625}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 34735], ['id', 39391], ['id', 31152], ['id', 57375], ['ood', 17502]], 'labels': [4, 8, 6, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.4357190132141113})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.6093339920043945})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.7189640998840332})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.8582508563995361})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7193, 'crossentropy': 1.261454296875}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 49619], ['ood', 36191], ['id', 31164], ['ood', 2384], ['ood', 55255]], 'labels': [7, 9, 4, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.389024019241333})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.4546653032302856})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.5934120416641235})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.6799498796463013})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7159, 'crossentropy': 1.25170869140625}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 9268], ['ood', 23273], ['id', 38726], ['id', 17376], ['ood', 45658]], 'labels': [1, 8, 5, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.226957082748413})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.4829368591308594})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.4584709405899048})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.631516456604004})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7407, 'crossentropy': 1.11657705078125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 14772], ['id', 53990], ['ood', 56359], ['id', 44323], ['id', 40308]], 'labels': [8, 4, 5, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.4122869968414307})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.5656269788742065})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.5162653923034668})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.8103365898132324})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7158, 'crossentropy': 1.285413671875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 49236], ['ood', 18349], ['id', 55994], ['ood', 37798], ['ood', 20737]], 'labels': [5, 4, 6, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.292983889579773})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.249274730682373})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4936985969543457})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.5159008502960205})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.5699806213378906})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7461, 'crossentropy': 1.19354814453125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 36999], ['id', 49149], ['id', 23649], ['ood', 16362], ['id', 27826]], 'labels': [5, 3, 3, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.2310128211975098})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.178248643875122})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.3506662845611572})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.426203727722168})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.4830313920974731})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7574, 'crossentropy': 1.14611123046875}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 16287], ['id', 27176], ['id', 52410], ['id', 47683], ['ood', 44688]], 'labels': [1, 5, 2, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.3144783973693848})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.4285047054290771})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.6791634559631348})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.6609339714050293})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7014, 'crossentropy': 1.20854375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 52593], ['id', 30526], ['ood', 3299], ['id', 53133], ['ood', 23391]], 'labels': [0, 6, 5, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.1653294563293457})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.2450382709503174})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.3949452638626099})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.3767145872116089})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7492, 'crossentropy': 1.0437943359375}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 34238], ['id', 10846], ['ood', 15248], ['id', 49726], ['id', 58405]], 'labels': [5, 2, 8, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.150519609451294})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2088844776153564})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.4739995002746582})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.5160094499588013})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7474, 'crossentropy': 1.0609962890625}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 28837], ['ood', 51797], ['ood', 31808], ['id', 45959], ['id', 5836]], 'labels': [8, 2, 9, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.0928008556365967})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.2047172784805298})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.1932027339935303})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.3404641151428223})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7661, 'crossentropy': 0.972790234375}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 20077], ['ood', 50553], ['ood', 35709], ['ood', 35145], ['id', 50053]], 'labels': [2, 6, 6, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0201570987701416})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.9978737831115723})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.1096354722976685})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0108579397201538})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.1776649951934814})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8059, 'crossentropy': 0.878804296875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 33756], ['id', 14321], ['ood', 30534], ['id', 57392], ['id', 12704]], 'labels': [9, 1, 0, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.0582165718078613})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0091521739959717})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.1561505794525146})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.2778668403625488})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.1881136894226074})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8034, 'crossentropy': 0.9118568359375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 50883], ['ood', 37348], ['id', 35060], ['ood', 23089], ['ood', 50517]], 'labels': [8, 8, 0, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9940448999404907})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9878123998641968})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.115794062614441})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0881482362747192})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1896319389343262})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.818, 'crossentropy': 0.87313154296875}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 24469], ['ood', 52041], ['id', 22], ['ood', 2850], ['ood', 36981]], 'labels': [3, 1, 9, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9606167078018188})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0167715549468994})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0698987245559692})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0588734149932861})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8034, 'crossentropy': 0.84792099609375}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 43668], ['ood', 33369], ['ood', 16048], ['ood', 22008], ['ood', 43654]], 'labels': [9, 7, 7, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0778311491012573})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.944429874420166})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9975523948669434})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0592509508132935})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1490851640701294})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8265, 'crossentropy': 0.84532958984375}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 17572], ['ood', 55775], ['id', 55088], ['id', 13172], ['id', 30423]], 'labels': [7, 1, 7, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8631953001022339})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8953390121459961})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9229405522346497})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0156186819076538})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8331, 'crossentropy': 0.814797607421875}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 9264], ['id', 18866], ['id', 11061], ['id', 19699], ['ood', 38775]], 'labels': [2, 4, 1, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9734215140342712})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8628947734832764})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9248409271240234})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9659216403961182})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0396003723144531})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8371, 'crossentropy': 0.791366650390625}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 49579], ['id', 22947], ['ood', 36007], ['id', 41055], ['id', 34241]], 'labels': [2, 9, 4, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.0051478147506714})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.980451226234436})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9994732141494751})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0662497282028198})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1071839332580566})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.818, 'crossentropy': 0.86933212890625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 30868], ['ood', 22283], ['ood', 28363], ['ood', 12185], ['id', 13208]], 'labels': [4, 0, 1, 0, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.024972677230835})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0022038221359253})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9658181667327881})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0297964811325073})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.09116530418396})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.2734519243240356})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8256, 'crossentropy': 0.8789009765625}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 59976], ['ood', 47256], ['ood', 21316], ['ood', 46920], ['id', 31869]], 'labels': [4, 4, 9, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9541916251182556})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9037482738494873})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0045552253723145})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0155651569366455})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1648321151733398})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8265, 'crossentropy': 0.806491357421875}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 23015], ['ood', 56045], ['id', 30809], ['ood', 5426], ['id', 53305]], 'labels': [7, 4, 1, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.0121530294418335})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.941306471824646})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9476804733276367})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0323586463928223})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0468535423278809})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8206, 'crossentropy': 0.82723310546875}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 33605], ['id', 5366], ['ood', 19444], ['ood', 47238], ['id', 42881]], 'labels': [8, 4, 5, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9792656898498535})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8955850601196289})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9531131982803345})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9393759369850159})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0736844539642334})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.826, 'crossentropy': 0.8210052734375}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 25971], ['id', 38242], ['ood', 54697], ['ood', 25420], ['ood', 50992]], 'labels': [3, 7, 9, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.9684462547302246})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8958609700202942})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0037578344345093})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0974597930908203})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1297359466552734})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8255, 'crossentropy': 0.8021384765625}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 28233], ['id', 6380], ['id', 36121], ['id', 46275], ['id', 13139]], 'labels': [8, 1, 8, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.9595462083816528})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.8296659588813782})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9554702043533325})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.001809000968933})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0845296382904053})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8242, 'crossentropy': 0.818495556640625}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 29180], ['ood', 50725], ['ood', 52843], ['ood', 2120], ['id', 57865]], 'labels': [9, 1, 4, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.021436333656311})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9581187963485718})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1302093267440796})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0419789552688599})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9958041906356812})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8333, 'crossentropy': 0.764798486328125}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 20816], ['id', 24123], ['ood', 29417], ['ood', 55737], ['id', 29346]], 'labels': [1, 8, 9, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.0302866697311401})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8554654121398926})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8466425538063049})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9120843410491943})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.034252405166626})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.1021473407745361})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.83, 'crossentropy': 0.80037353515625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 46308], ['ood', 2264], ['id', 46929], ['ood', 51845], ['ood', 51991]], 'labels': [9, 4, 9, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.0400516986846924})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8413021564483643})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8869001865386963})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9327555894851685})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0594066381454468})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8417, 'crossentropy': 0.7561318359375}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 27202], ['ood', 16716], ['ood', 49118], ['ood', 52539], ['id', 8580]], 'labels': [4, 3, 2, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.0003737211227417})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9105315208435059})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8475989103317261})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9718582630157471})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9593738317489624})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1219823360443115})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8494, 'crossentropy': 0.7704177734375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 25718], ['id', 18738], ['id', 46897], ['ood', 46495], ['id', 27651]], 'labels': [2, 9, 8, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 0.9762150049209595})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.839666485786438})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.8800574541091919})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8679183721542358})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8216571807861328})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9093577861785889})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0408793687820435})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9200769662857056})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8602, 'crossentropy': 0.733936376953125}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 17619], ['ood', 41089], ['ood', 51830], ['id', 8575], ['ood', 23775]], 'labels': [8, 4, 3, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.9667624235153198})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8619153499603271})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.823290228843689})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8807969093322754})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9251829981803894})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.094775915145874})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.85, 'crossentropy': 0.7486802734375}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 55118], ['ood', 57880], ['id', 30555], ['id', 58118], ['id', 23989]], 'labels': [7, 4, 0, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9329848885536194})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9504132270812988})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8494541645050049})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9544404745101929})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8905465006828308})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9821316599845886})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.858, 'crossentropy': 0.74239140625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 31219], ['id', 5646], ['ood', 16429], ['ood', 54790], ['id', 21671]], 'labels': [7, 0, 4, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.9979763031005859})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.7856416702270508})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8433454036712646})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8888536691665649})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9191628694534302})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8416, 'crossentropy': 0.74435234375}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 46307], ['ood', 54189], ['ood', 27755], ['ood', 6317], ['id', 42884]], 'labels': [5, 6, 2, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9018079042434692})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7055431008338928})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8208840489387512})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7933782339096069})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8671321868896484})
store['active_learning_steps'][37]['training']['best_epoch']=2
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.862, 'crossentropy': 0.66409951171875}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 7434], ['ood', 42683], ['ood', 21430], ['id', 30012], ['ood', 17109]], 'labels': [6, 0, 6, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0039340257644653})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8114584684371948})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7347245216369629})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8234411478042603})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.753846287727356})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7814919948577881})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8651, 'crossentropy': 0.662752685546875}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 37270], ['id', 12823], ['id', 532], ['id', 38926], ['ood', 39468]], 'labels': [5, 2, 8, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8429681062698364})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.748146116733551})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7976548075675964})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7533679008483887})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8107998371124268})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8498, 'crossentropy': 0.674219873046875}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 52560], ['ood', 57423], ['id', 1059], ['ood', 20454], ['ood', 22741]], 'labels': [7, 0, 8, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8544830083847046})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7068827748298645})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8265829682350159})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7763152718544006})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8154075741767883})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8631, 'crossentropy': 0.65086376953125}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 50845], ['id', 46573], ['ood', 6615], ['id', 37184], ['id', 22100]], 'labels': [5, 8, 4, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9252572059631348})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7406570911407471})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7545491456985474})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7832720279693604})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8208600282669067})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8586, 'crossentropy': 0.666352734375}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 26493], ['id', 11135], ['id', 13662], ['id', 33546], ['ood', 5511]], 'labels': [5, 1, 7, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9430886507034302})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7407770156860352})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7838950157165527})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8038750886917114})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7994517087936401})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8518, 'crossentropy': 0.70042177734375}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 37529], ['id', 36631], ['ood', 55241], ['ood', 37805], ['id', 9626]], 'labels': [8, 2, 2, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8847324252128601})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.771294116973877})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7716925144195557})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.812323808670044})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8321685194969177})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8578, 'crossentropy': 0.66465380859375}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 14574], ['id', 44413], ['ood', 33015], ['id', 13297], ['id', 12495]], 'labels': [0, 0, 2, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9111238718032837})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7846382856369019})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7372419834136963})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8448120355606079})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7362133264541626})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8465024828910828})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8713208436965942})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9105564951896667})
store['active_learning_steps'][44]['training']['best_epoch']=5
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8771, 'crossentropy': 0.676212548828125}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 12310], ['id', 14200], ['ood', 35251], ['ood', 56832], ['ood', 559]], 'labels': [7, 3, 2, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.9835212230682373})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7441266775131226})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7354070544242859})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7498789429664612})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7695896029472351})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7714657783508301})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8669, 'crossentropy': 0.666712109375}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 35425], ['ood', 52657], ['ood', 57187], ['ood', 45651], ['ood', 56949]], 'labels': [7, 1, 2, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9024403095245361})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8393046855926514})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7200014591217041})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7180566787719727})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7990365624427795})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8325345516204834})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.826598048210144})
store['active_learning_steps'][46]['training']['best_epoch']=4
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.879, 'crossentropy': 0.643269921875}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 58833], ['ood', 5566], ['id', 6504], ['id', 56173], ['id', 18265]], 'labels': [4, 7, 5, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8421858549118042})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7335659861564636})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.694236159324646})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.767235279083252})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8370276689529419})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7478430271148682})
store['active_learning_steps'][47]['training']['best_epoch']=3
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8754, 'crossentropy': 0.6195109375}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 31380], ['id', 10263], ['id', 6828], ['id', 21677], ['ood', 11062]], 'labels': [8, 7, 6, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7807257175445557})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6951547861099243})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6882988810539246})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6967084407806396})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7702475786209106})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7279319763183594})
store['active_learning_steps'][48]['training']['best_epoch']=3
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8838, 'crossentropy': 0.591346875}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 47349], ['ood', 53312], ['id', 25200], ['id', 58846], ['ood', 42949]], 'labels': [7, 3, 7, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9481519460678101})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7301361560821533})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7096664905548096})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7122495174407959})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7078303098678589})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7590843439102173})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8161008358001709})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8009776473045349})
store['active_learning_steps'][49]['training']['best_epoch']=5
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8954, 'crossentropy': 0.60727421875}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 3920], ['ood', 20252], ['id', 1963], ['id', 15772], ['ood', 59740]], 'labels': [7, 4, 0, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8258135318756104})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6910010576248169})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7056124210357666})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6574140191078186})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.647741436958313})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.679426908493042})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7959266304969788})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7608656883239746})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8845, 'crossentropy': 0.62549130859375}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 31775], ['id', 15337], ['id', 25911], ['id', 5071], ['id', 37223]], 'labels': [3, 5, 3, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8608110547065735})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6844407320022583})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6315967440605164})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6666238903999329})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7010428309440613})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7406826019287109})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8923, 'crossentropy': 0.55567783203125}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 25392], ['ood', 47834], ['id', 3980], ['ood', 38569], ['id', 35963]], 'labels': [1, 3, 2, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8405881524085999})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6448681950569153})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6047396063804626})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6345360279083252})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6387776136398315})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6486716270446777})
store['active_learning_steps'][52]['training']['best_epoch']=3
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8913, 'crossentropy': 0.563709228515625}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 7894], ['ood', 36713], ['id', 31565], ['id', 53818], ['id', 45597]], 'labels': [5, 9, 9, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7903721332550049})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5869266986846924})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5794897079467773})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6166442632675171})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.619891881942749})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.640203595161438})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8986, 'crossentropy': 0.531061279296875}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 12994], ['id', 52603], ['id', 18038], ['id', 9373], ['ood', 392]], 'labels': [7, 7, 2, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7881355285644531})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6453338861465454})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6028860211372375})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6021111607551575})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6700644493103027})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.747770369052887})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6782448291778564})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8994, 'crossentropy': 0.54884228515625}
store['active_learning_steps'][54]['acquisition']={'indices': [['id', 8884], ['ood', 8959], ['id', 52546], ['ood', 45279], ['id', 1116]], 'labels': [3, 3, 9, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8460108041763306})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6417325735092163})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5654197931289673})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6313154697418213})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6498450040817261})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.660329282283783})
store['active_learning_steps'][55]['training']['best_epoch']=3
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.896, 'crossentropy': 0.528266162109375}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 57035], ['id', 41558], ['id', 5254], ['id', 37842], ['id', 45810]], 'labels': [4, 7, 5, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8095163106918335})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6163085699081421})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6279864311218262})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.605086088180542})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6679195761680603})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6645045280456543})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6664634943008423})
store['active_learning_steps'][56]['training']['best_epoch']=4
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.5619849609375}
store['active_learning_steps'][56]['acquisition']={'indices': [['id', 28342], ['id', 42467], ['ood', 4138], ['id', 44981], ['ood', 28532]], 'labels': [8, 8, 0, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8018068075180054})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6711830496788025})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5915178656578064})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6006432771682739})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6278344988822937})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6073704957962036})
store['active_learning_steps'][57]['training']['best_epoch']=3
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8957, 'crossentropy': 0.5370802734375}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 54695], ['id', 5977], ['id', 20325], ['ood', 27732], ['ood', 42304]], 'labels': [1, 8, 5, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8121224641799927})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6546726226806641})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.645065426826477})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5886207818984985})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6723020076751709})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6229922771453857})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7048628330230713})
store['active_learning_steps'][58]['training']['best_epoch']=4
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9024, 'crossentropy': 0.549610986328125}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 22156], ['id', 37854], ['ood', 10350], ['id', 44007], ['id', 22166]], 'labels': [5, 0, 5, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7409837245941162})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5621755123138428})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5856454372406006})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5577199459075928})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6475046873092651})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6571063995361328})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6675444841384888})
store['active_learning_steps'][59]['training']['best_epoch']=4
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9141, 'crossentropy': 0.499561181640625}
store['active_learning_steps'][59]['acquisition']={'indices': [['ood', 47453], ['ood', 20402], ['ood', 51094], ['id', 27139], ['id', 11264]], 'labels': [2, 1, 3, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7769429683685303})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6058380603790283})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5732901096343994})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6155011653900146})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5793600082397461})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5920645594596863})
store['active_learning_steps'][60]['training']['best_epoch']=3
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9046, 'crossentropy': 0.51515341796875}
store['active_learning_steps'][60]['acquisition']={'indices': [['ood', 31335], ['ood', 51131], ['ood', 49863], ['ood', 34112], ['id', 30328]], 'labels': [1, 1, 8, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8898274302482605})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5742409229278564})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5700200796127319})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6164255142211914})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5698780417442322})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6824454069137573})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6458523273468018})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7039052248001099})
store['active_learning_steps'][61]['training']['best_epoch']=5
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.508906005859375}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 13436], ['id', 24162], ['ood', 372], ['ood', 27296], ['ood', 35864]], 'labels': [8, 6, 8, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8218240737915039})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5689085721969604})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6143347024917603})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6346275806427002})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6321873664855957})
store['active_learning_steps'][62]['training']['best_epoch']=2
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9035, 'crossentropy': 0.51690380859375}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 24230], ['id', 14585], ['ood', 41319], ['ood', 33965], ['id', 4579]], 'labels': [9, 1, 1, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.847574770450592})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5739560723304749})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6143193244934082})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6250259280204773})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6444813013076782})
store['active_learning_steps'][63]['training']['best_epoch']=2
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9004, 'crossentropy': 0.556630126953125}
store['active_learning_steps'][63]['acquisition']={'indices': [['ood', 24958], ['id', 48754], ['ood', 41713], ['ood', 25958], ['ood', 11169]], 'labels': [1, 4, 8, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7998241186141968})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5865776538848877})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.557077944278717})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5667405128479004})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.641389012336731})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5538361668586731})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6495999097824097})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6155674457550049})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6785539984703064})
store['active_learning_steps'][64]['training']['best_epoch']=6
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9192, 'crossentropy': 0.510087744140625}
store['active_learning_steps'][64]['acquisition']={'indices': [['ood', 54064], ['id', 12464], ['id', 47961], ['ood', 48883], ['ood', 1602]], 'labels': [5, 7, 4, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7330864667892456})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5613501071929932})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5475608110427856})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5530281066894531})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5510671138763428})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6998587250709534})
store['active_learning_steps'][65]['training']['best_epoch']=3
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9101, 'crossentropy': 0.476186083984375}
store['active_learning_steps'][65]['acquisition']={'indices': [['ood', 58038], ['ood', 58455], ['ood', 22437], ['ood', 59555], ['id', 47237]], 'labels': [0, 9, 0, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8311864137649536})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6010518074035645})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5500240325927734})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6022709608078003})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6234091520309448})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5554924607276917})
store['active_learning_steps'][66]['training']['best_epoch']=3
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.4875169921875}
store['active_learning_steps'][66]['acquisition']={'indices': [['id', 55387], ['id', 17102], ['id', 37680], ['ood', 28240], ['ood', 43170]], 'labels': [6, 4, 5, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.882243812084198})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6047084331512451})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5801937580108643})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6086399555206299})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.627321720123291})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6041512489318848})
store['active_learning_steps'][67]['training']['best_epoch']=3
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9049, 'crossentropy': 0.50388681640625}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 22170], ['ood', 33804], ['ood', 8393], ['ood', 57154], ['ood', 21223]], 'labels': [1, 8, 6, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8121956586837769})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5843355059623718})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5836225748062134})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6509802341461182})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6301509141921997})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.555286169052124})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6544716358184814})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6657555103302002})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7394769191741943})
store['active_learning_steps'][68]['training']['best_epoch']=6
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9161, 'crossentropy': 0.502984033203125}
store['active_learning_steps'][68]['acquisition']={'indices': [['ood', 57769], ['id', 48722], ['ood', 24563], ['ood', 41664], ['ood', 37405]], 'labels': [5, 3, 1, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7921785116195679})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5961235761642456})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5829563140869141})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5700466632843018})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5807165503501892})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.594504714012146})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6217418909072876})
store['active_learning_steps'][69]['training']['best_epoch']=4
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9082, 'crossentropy': 0.515882275390625}
store['active_learning_steps'][69]['acquisition']={'indices': [['id', 13698], ['ood', 19784], ['id', 13816], ['id', 20440], ['id', 27678]], 'labels': [9, 7, 0, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.780608057975769})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6275942921638489})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5850434303283691})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6005393862724304})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6215674877166748})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6590297222137451})
store['active_learning_steps'][70]['training']['best_epoch']=3
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8984, 'crossentropy': 0.5469212890625}
store['active_learning_steps'][70]['acquisition']={'indices': [['ood', 48983], ['ood', 57367], ['id', 54029], ['ood', 7635], ['ood', 16529]], 'labels': [3, 0, 3, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8545476198196411})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.61549311876297})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5910388231277466})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.673789381980896})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6898077130317688})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5853407382965088})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6380400657653809})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7244020700454712})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6610715985298157})
store['active_learning_steps'][71]['training']['best_epoch']=6
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9111, 'crossentropy': 0.534177197265625}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 49871], ['ood', 14237], ['id', 3950], ['ood', 25234], ['ood', 6366]], 'labels': [9, 4, 6, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7858215570449829})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6133065223693848})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6100664138793945})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5797511339187622})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6190551519393921})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6576328873634338})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6664820313453674})
store['active_learning_steps'][72]['training']['best_epoch']=4
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9105, 'crossentropy': 0.49188525390625}
store['active_learning_steps'][72]['acquisition']={'indices': [['id', 43709], ['id', 4464], ['ood', 4259], ['id', 6985], ['id', 50692]], 'labels': [4, 4, 7, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8150457739830017})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6638532876968384})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6380711793899536})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5521183013916016})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6403002738952637})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6206873655319214})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6390819549560547})
store['active_learning_steps'][73]['training']['best_epoch']=4
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9146, 'crossentropy': 0.484704052734375}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 13143], ['ood', 59437], ['id', 15411], ['id', 50668], ['id', 46]], 'labels': [4, 5, 8, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7977371215820312})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5894362926483154})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.538724958896637})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5956187844276428})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5672657489776611})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5907045006752014})
store['active_learning_steps'][74]['training']['best_epoch']=3
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9112, 'crossentropy': 0.500469970703125}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 31398], ['id', 37906], ['ood', 42221], ['id', 38271], ['ood', 41199]], 'labels': [7, 9, 7, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8298393487930298})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6198751330375671})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5929293632507324})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5872282981872559})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5745447874069214})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5922794342041016})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.588533341884613})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6937004327774048})
store['active_learning_steps'][75]['training']['best_epoch']=5
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9111, 'crossentropy': 0.53476328125}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 15518], ['ood', 26692], ['id', 21883], ['ood', 32290], ['ood', 5876]], 'labels': [8, 9, 5, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.878464937210083})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6268665790557861})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5805700421333313})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6113331317901611})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5666451454162598})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6222749948501587})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6591188907623291})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6628203392028809})
store['active_learning_steps'][76]['training']['best_epoch']=5
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9154, 'crossentropy': 0.51039931640625}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 46271], ['ood', 2071], ['ood', 7846], ['ood', 54062], ['id', 52286]], 'labels': [9, 1, 1, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8251124620437622})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5882498025894165})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5284587740898132})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5828675031661987})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.55240797996521})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7083496451377869})
store['active_learning_steps'][77]['training']['best_epoch']=3
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.918, 'crossentropy': 0.457418359375}
store['active_learning_steps'][77]['acquisition']={'indices': [['ood', 26840], ['id', 30061], ['ood', 8286], ['id', 36905], ['ood', 17254]], 'labels': [8, 5, 1, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8310763239860535})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5784276723861694})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5332533121109009})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5078754425048828})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5566887855529785})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5653916001319885})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5471781492233276})
store['active_learning_steps'][78]['training']['best_epoch']=4
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.922, 'crossentropy': 0.45597177734375}
store['active_learning_steps'][78]['acquisition']={'indices': [['id', 9738], ['ood', 45960], ['ood', 38765], ['id', 34677], ['id', 9731]], 'labels': [5, 5, 3, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9507005214691162})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5688366889953613})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.581426739692688})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5260600447654724})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5272508263587952})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5532749891281128})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5606629848480225})
store['active_learning_steps'][79]['training']['best_epoch']=4
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9159, 'crossentropy': 0.475454638671875}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 45466], ['ood', 43352], ['ood', 1848], ['ood', 12420], ['ood', 2380]], 'labels': [7, 4, 5, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8151551485061646})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5931394696235657})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.511992335319519})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5858927965164185})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5429000854492188})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5142307281494141})
store['active_learning_steps'][80]['training']['best_epoch']=3
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9143, 'crossentropy': 0.482666064453125}
store['active_learning_steps'][80]['acquisition']={'indices': [['ood', 50838], ['ood', 29738], ['ood', 33647], ['id', 14422], ['ood', 47332]], 'labels': [3, 1, 2, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8422439098358154})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.583258867263794})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5441915392875671})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5432113409042358})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5256003141403198})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5505433678627014})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5805922150611877})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.612171471118927})
store['active_learning_steps'][81]['training']['best_epoch']=5
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9203, 'crossentropy': 0.472120654296875}
store['active_learning_steps'][81]['acquisition']={'indices': [['ood', 40735], ['id', 434], ['ood', 1051], ['ood', 11479], ['ood', 50179]], 'labels': [6, 9, 9, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8390898108482361})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5860779285430908})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5417909622192383})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5925690531730652})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.49514299631118774})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5566116571426392})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5447973012924194})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5599860548973083})
store['active_learning_steps'][82]['training']['best_epoch']=5
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9196, 'crossentropy': 0.466025146484375}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 12388], ['ood', 47876], ['id', 14339], ['ood', 57329], ['id', 44843]], 'labels': [1, 0, 6, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8327595591545105})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5738688111305237})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.48439520597457886})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5219703912734985})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5741220712661743})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5057556629180908})
store['active_learning_steps'][83]['training']['best_epoch']=3
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9152, 'crossentropy': 0.4664384765625}
store['active_learning_steps'][83]['acquisition']={'indices': [['ood', 17256], ['id', 21709], ['id', 32675], ['id', 13911], ['id', 48391]], 'labels': [0, 1, 1, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8767603635787964})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5862029790878296})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5737073421478271})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.595596194267273})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5339893102645874})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5398260951042175})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5399968028068542})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6044389009475708})
store['active_learning_steps'][84]['training']['best_epoch']=5
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9144, 'crossentropy': 0.50778388671875}
store['active_learning_steps'][84]['acquisition']={'indices': [['id', 34877], ['ood', 55490], ['id', 10029], ['ood', 43371], ['id', 9697]], 'labels': [5, 5, 2, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.836570680141449})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5931691527366638})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.564163327217102})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.49981236457824707})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5950905084609985})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5494930744171143})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5998257994651794})
store['active_learning_steps'][85]['training']['best_epoch']=4
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.4608490234375}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 40584], ['ood', 26970], ['id', 44380], ['ood', 14844], ['ood', 5370]], 'labels': [9, 4, 3, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8540475368499756})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5616832971572876})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5323038697242737})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5362970232963562})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5612993240356445})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5364879369735718})
store['active_learning_steps'][86]['training']['best_epoch']=3
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9123, 'crossentropy': 0.49192568359375}
