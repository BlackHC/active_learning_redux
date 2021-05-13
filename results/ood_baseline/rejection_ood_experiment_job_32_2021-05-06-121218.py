store = {}
store['timestamp']=1620299538
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=32']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=32
store['worker_id']=32
store['num_workers']=40
store['config']={'seed': 44, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.403069496154785})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.7887887954711914})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.8772222995758057})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.008791923522949})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6582, 'crossentropy': 2.2032611328125}
store['active_learning_steps'][0]['acquisition']={'indices': [34368, 2330, 21255, 19589, 52402], 'labels': [3, 5, 2, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.4437174797058105})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.8783998489379883})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.8571958541870117})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.2087082862854004})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6498, 'crossentropy': 2.3066283203125}
store['active_learning_steps'][1]['acquisition']={'indices': [53425, 36659, 18503, 45027, 19862], 'labels': [-1, 4, 3, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.802454948425293})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.198512315750122})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.4729256629943848})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.41139554977417})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7347, 'crossentropy': 1.6804669921875}
store['active_learning_steps'][2]['acquisition']={'indices': [50428, 50821, 25835, 9876, 4958], 'labels': [-1, -1, -1, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.219839572906494})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.7023658752441406})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.60654878616333})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.6406021118164062})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.704, 'crossentropy': 1.8154767578125}
store['active_learning_steps'][3]['acquisition']={'indices': [45265, 32285, 6653, 15464, 43770], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.276340961456299})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.1720688343048096})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.203885078430176})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.645944595336914})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.3564369678497314})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7151, 'crossentropy': 2.082098046875}
store['active_learning_steps'][4]['acquisition']={'indices': [41071, 11535, 22031, 36539, 36614], 'labels': [-1, 3, 4, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.2403554916381836})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.447704315185547})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.814927101135254})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.689514636993408})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7031, 'crossentropy': 1.919862109375}
store['active_learning_steps'][5]['acquisition']={'indices': [43008, 21569, 42146, 50877, 44977], 'labels': [-1, -1, 7, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.8991732597351074})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.5009946823120117})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.6113662719726562})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.6463091373443604})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7411, 'crossentropy': 1.6265474609375}
store['active_learning_steps'][6]['acquisition']={'indices': [9031, 5891, 58682, 48362, 56908], 'labels': [2, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.7479822635650635})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.2885453701019287})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.2035558223724365})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.5080156326293945})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7368, 'crossentropy': 1.57741494140625}
store['active_learning_steps'][7]['acquisition']={'indices': [49082, 6909, 19920, 41207, 17396], 'labels': [3, -1, 5, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.1318140029907227})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.124069929122925})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.680595874786377})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.7738149166107178})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.69515061378479})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7153, 'crossentropy': 1.9491302734375}
store['active_learning_steps'][8]['acquisition']={'indices': [16817, 35259, 25406, 7313, 38092], 'labels': [0, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.5543761253356934})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.9106019735336304})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.8900525569915771})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.262838840484619})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7413, 'crossentropy': 1.417226953125}
store['active_learning_steps'][9]['acquisition']={'indices': [54585, 42500, 18983, 30606, 31796], 'labels': [-1, 9, 1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.480517864227295})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.6273462772369385})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.9520339965820312})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.865082025527954})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7639, 'crossentropy': 1.294909375}
store['active_learning_steps'][10]['acquisition']={'indices': [54335, 41419, 56442, 43251, 58162], 'labels': [-1, 1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.4248311519622803})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.4641425609588623})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.6638576984405518})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.6340601444244385})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.79, 'crossentropy': 1.22829521484375}
store['active_learning_steps'][11]['acquisition']={'indices': [21969, 28127, 46480, 19292, 59574], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.4350111484527588})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.5830117464065552})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.7858258485794067})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.7653591632843018})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7897, 'crossentropy': 1.25166005859375}
store['active_learning_steps'][12]['acquisition']={'indices': [656, 14040, 21931, 56427, 20512], 'labels': [0, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.4762444496154785})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.4992986917495728})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.6733572483062744})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.8669540882110596})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7927, 'crossentropy': 1.3174078125}
store['active_learning_steps'][13]['acquisition']={'indices': [57925, 41621, 47284, 38908, 43546], 'labels': [7, 8, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1422102451324463})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2992844581604004})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.311625599861145})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4808628559112549})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8233, 'crossentropy': 1.0315150390625}
store['active_learning_steps'][14]['acquisition']={'indices': [7808, 38557, 19464, 10687, 36101], 'labels': [-1, -1, -1, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1679637432098389})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.3223811388015747})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.3777246475219727})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.4755096435546875})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8194, 'crossentropy': 1.07670048828125}
store['active_learning_steps'][15]['acquisition']={'indices': [7582, 20860, 34327, 32271, 8537], 'labels': [3, 5, 3, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0338184833526611})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2282631397247314})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.2456247806549072})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2801152467727661})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8462, 'crossentropy': 0.94016044921875}
store['active_learning_steps'][16]['acquisition']={'indices': [31546, 17094, 39349, 33331, 36752], 'labels': [-1, -1, -1, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.0255794525146484})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0922306776046753})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1936023235321045})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2409732341766357})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8154, 'crossentropy': 0.95904599609375}
store['active_learning_steps'][17]['acquisition']={'indices': [27859, 53407, 46781, 2106, 20641], 'labels': [0, -1, -1, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0286271572113037})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2217237949371338})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.162646770477295})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.3037092685699463})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8263, 'crossentropy': 0.98892099609375}
store['active_learning_steps'][18]['acquisition']={'indices': [10006, 17501, 27460, 4868, 35225], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0226343870162964})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3185334205627441})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.124326229095459})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1823869943618774})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8343, 'crossentropy': 0.90593984375}
store['active_learning_steps'][19]['acquisition']={'indices': [36080, 13511, 22164, 51683, 28682], 'labels': [9, 6, 1, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8183750510215759})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0653239488601685})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.094064474105835})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.131537675857544})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8574, 'crossentropy': 0.782588623046875}
store['active_learning_steps'][20]['acquisition']={'indices': [32256, 46510, 38102, 4387, 4070], 'labels': [9, 2, 0, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9412840604782104})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9786232709884644})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0600992441177368})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1969127655029297})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8472, 'crossentropy': 0.878580078125}
store['active_learning_steps'][21]['acquisition']={'indices': [53759, 49884, 22648, 47669, 44544], 'labels': [-1, 1, -1, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9139320254325867})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.055631160736084})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.115408182144165})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.2892308235168457})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8415, 'crossentropy': 0.84795947265625}
store['active_learning_steps'][22]['acquisition']={'indices': [16658, 8643, 15766, 46153, 6500], 'labels': [-1, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.803874671459198})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9537754058837891})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0658137798309326})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.116699457168579})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8609, 'crossentropy': 0.767481689453125}
store['active_learning_steps'][23]['acquisition']={'indices': [16744, 6927, 4415, 12489, 28949], 'labels': [2, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8676140308380127})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1277518272399902})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1281925439834595})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.168419599533081})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8392, 'crossentropy': 0.83684287109375}
store['active_learning_steps'][24]['acquisition']={'indices': [22484, 41696, 5797, 29235, 46987], 'labels': [-1, 0, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9017000198364258})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9560236930847168})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.037580132484436})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.121895670890808})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.847, 'crossentropy': 0.83951005859375}
store['active_learning_steps'][25]['acquisition']={'indices': [52573, 47595, 52518, 33996, 25852], 'labels': [-1, 7, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8648698329925537})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9281677007675171})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0228126049041748})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.042100429534912})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8531, 'crossentropy': 0.7916716796875}
store['active_learning_steps'][26]['acquisition']={'indices': [31023, 1734, 40988, 22564, 18613], 'labels': [8, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9122860431671143})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9233417510986328})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0550155639648438})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.036087155342102})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8462, 'crossentropy': 0.84036962890625}
store['active_learning_steps'][27]['acquisition']={'indices': [6773, 31268, 22731, 5622, 50073], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8969113230705261})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9303678870201111})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1127371788024902})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0289833545684814})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8465, 'crossentropy': 0.8695486328125}
store['active_learning_steps'][28]['acquisition']={'indices': [5877, 668, 31657, 57180, 33898], 'labels': [6, 0, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.908532977104187})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9422862529754639})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1059300899505615})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.2092514038085938})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.818, 'crossentropy': 0.91030791015625}
store['active_learning_steps'][29]['acquisition']={'indices': [26789, 20366, 39616, 47522, 18322], 'labels': [-1, -1, -1, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8342176675796509})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8883945345878601})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9479472041130066})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.211921215057373})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8445, 'crossentropy': 0.83158779296875}
store['active_learning_steps'][30]['acquisition']={'indices': [12610, 37543, 39308, 24053, 50232], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8819212913513184})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0283584594726562})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.2123637199401855})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.2092516422271729})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8551, 'crossentropy': 0.82338896484375}
store['active_learning_steps'][31]['acquisition']={'indices': [39319, 9140, 5593, 35051, 52597], 'labels': [-1, 3, 6, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9299269914627075})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0575087070465088})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.041215419769287})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1837244033813477})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8232, 'crossentropy': 0.879251171875}
store['active_learning_steps'][32]['acquisition']={'indices': [9148, 19697, 54148, 1359, 27514], 'labels': [4, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8969101309776306})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0728199481964111})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.037834644317627})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.1468180418014526})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8331, 'crossentropy': 0.8648408203125}
store['active_learning_steps'][33]['acquisition']={'indices': [49697, 26187, 3527, 34014, 46180], 'labels': [-1, -1, -1, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9151323437690735})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0140528678894043})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1678731441497803})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.2041354179382324})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8257, 'crossentropy': 0.88914296875}
store['active_learning_steps'][34]['acquisition']={'indices': [50193, 15550, 56732, 48253, 50479], 'labels': [6, -1, 5, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7914609909057617})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9883214235305786})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9868175387382507})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.045329213142395})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8535, 'crossentropy': 0.787333642578125}
store['active_learning_steps'][35]['acquisition']={'indices': [23729, 7167, 41671, 19479, 14578], 'labels': [8, -1, 4, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8067702054977417})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8467769622802734})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9686574935913086})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0440013408660889})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8635, 'crossentropy': 0.78944423828125}
store['active_learning_steps'][36]['acquisition']={'indices': [48969, 47981, 8237, 22271, 8870], 'labels': [7, 4, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8088775873184204})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8822648525238037})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9549367427825928})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9772570729255676})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8471, 'crossentropy': 0.81499482421875}
store['active_learning_steps'][37]['acquisition']={'indices': [24086, 7936, 35048, 41274, 28129], 'labels': [1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8342651128768921})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9218605756759644})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0649954080581665})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.1193795204162598})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.844, 'crossentropy': 0.83647216796875}
store['active_learning_steps'][38]['acquisition']={'indices': [26230, 58658, 38573, 38084, 37131], 'labels': [0, -1, -1, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.845236599445343})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8580693006515503})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8670938014984131})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9922571182250977})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8619, 'crossentropy': 0.765535400390625}
store['active_learning_steps'][39]['acquisition']={'indices': [4933, 6507, 41955, 34929, 48124], 'labels': [-1, 7, -1, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8496608734130859})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9052948951721191})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9840463995933533})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9573113322257996})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8456, 'crossentropy': 0.79974794921875}
store['active_learning_steps'][40]['acquisition']={'indices': [58139, 41872, 17059, 21837, 21311], 'labels': [-1, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8609121441841125})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8740112781524658})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9119240641593933})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9561002254486084})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8483, 'crossentropy': 0.8082658203125}
store['active_learning_steps'][41]['acquisition']={'indices': [35921, 54744, 25719, 16325, 15043], 'labels': [8, -1, 1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8487483263015747})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9045124650001526})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8837252855300903})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.100722074508667})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8418, 'crossentropy': 0.86251279296875}
store['active_learning_steps'][42]['acquisition']={'indices': [27497, 15507, 48235, 25327, 25555], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8758329153060913})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8026320934295654})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8483800888061523})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9923313856124878})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0003325939178467})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8767, 'crossentropy': 0.75646376953125}
store['active_learning_steps'][43]['acquisition']={'indices': [55629, 43884, 38357, 9969, 4945], 'labels': [2, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.93277508020401})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8647266626358032})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1196163892745972})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0257902145385742})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 1.089400053024292})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8719, 'crossentropy': 0.84219326171875}
store['active_learning_steps'][44]['acquisition']={'indices': [15133, 32343, 40778, 37673, 21917], 'labels': [0, 5, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8249205350875854})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9636198282241821})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8703492879867554})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0875706672668457})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8573, 'crossentropy': 0.774896484375}
store['active_learning_steps'][45]['acquisition']={'indices': [56697, 50335, 10758, 55308, 58481], 'labels': [-1, 2, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8706637024879456})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8455027341842651})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8484145402908325})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9244559407234192})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9522099494934082})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8799, 'crossentropy': 0.7814544921875}
store['active_learning_steps'][46]['acquisition']={'indices': [34956, 55318, 9584, 21338, 43739], 'labels': [6, -1, 1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7775600552558899})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.807517409324646})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9372788667678833})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0572421550750732})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8448, 'crossentropy': 0.769164404296875}
store['active_learning_steps'][47]['acquisition']={'indices': [1769, 48176, 31512, 7707, 35781], 'labels': [-1, -1, -1, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8245655298233032})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8821637034416199})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9281779527664185})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9779766798019409})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.858, 'crossentropy': 0.79873115234375}
store['active_learning_steps'][48]['acquisition']={'indices': [33535, 54355, 14055, 53878, 4076], 'labels': [1, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7804521322250366})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8805240392684937})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9537721872329712})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9787088632583618})
store['active_learning_steps'][49]['training']['best_epoch']=1
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8725, 'crossentropy': 0.7167466796875}
store['active_learning_steps'][49]['acquisition']={'indices': [37028, 36877, 30407, 11610, 6627], 'labels': [-1, 4, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7647459506988525})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7973884344100952})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8522427678108215})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0981240272521973})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8725, 'crossentropy': 0.719987939453125}
store['active_learning_steps'][50]['acquisition']={'indices': [15979, 56995, 25001, 34182, 23529], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7898871898651123})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7829726934432983})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9093028903007507})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0398290157318115})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0086214542388916})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8617, 'crossentropy': 0.8217525390625}
store['active_learning_steps'][51]['acquisition']={'indices': [29685, 57607, 18729, 17445, 9128], 'labels': [5, -1, 7, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8120063543319702})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7725005149841309})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8803662657737732})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0887750387191772})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8755285143852234})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8858, 'crossentropy': 0.752896533203125}
store['active_learning_steps'][52]['acquisition']={'indices': [42462, 37519, 10343, 29192, 5082], 'labels': [1, -1, 0, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7383359670639038})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7755593061447144})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9283362627029419})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.990411639213562})
store['active_learning_steps'][53]['training']['best_epoch']=1
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8479, 'crossentropy': 0.74783564453125}
store['active_learning_steps'][53]['acquisition']={'indices': [59890, 35942, 46474, 43064, 30915], 'labels': [9, -1, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8311231136322021})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8242138624191284})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9914621114730835})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9707687497138977})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0286582708358765})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8847, 'crossentropy': 0.734040625}
store['active_learning_steps'][54]['acquisition']={'indices': [7847, 6236, 33351, 43008, 19648], 'labels': [6, 6, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7417632341384888})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7908390760421753})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8371155261993408})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9097975492477417})
store['active_learning_steps'][55]['training']['best_epoch']=1
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.86, 'crossentropy': 0.756570751953125}
store['active_learning_steps'][55]['acquisition']={'indices': [38694, 12422, 49796, 55397, 9522], 'labels': [6, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7899318933486938})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7925131320953369})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8790446519851685})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.0569393634796143})
store['active_learning_steps'][56]['training']['best_epoch']=1
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8506, 'crossentropy': 0.789985595703125}
store['active_learning_steps'][56]['acquisition']={'indices': [50242, 1712, 19710, 14793, 21192], 'labels': [-1, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8349120616912842})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9132194519042969})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8926384449005127})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8766160011291504})
store['active_learning_steps'][57]['training']['best_epoch']=1
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8409, 'crossentropy': 0.84980966796875}
store['active_learning_steps'][57]['acquisition']={'indices': [35804, 21262, 21180, 31704, 59527], 'labels': [9, 4, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.798335075378418})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7752078771591187})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8370054364204407})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9222006797790527})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.019788146018982})
store['active_learning_steps'][58]['training']['best_epoch']=2
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8782, 'crossentropy': 0.731941162109375}
store['active_learning_steps'][58]['acquisition']={'indices': [40367, 19986, 58994, 49609, 56554], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.775521457195282})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7908841967582703})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8805186748504639})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8384882211685181})
store['active_learning_steps'][59]['training']['best_epoch']=1
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8595, 'crossentropy': 0.74840185546875}
store['active_learning_steps'][59]['acquisition']={'indices': [23766, 17725, 54865, 52400, 54959], 'labels': [6, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.841292142868042})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8686776161193848})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9231282472610474})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9603731632232666})
store['active_learning_steps'][60]['training']['best_epoch']=1
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8671, 'crossentropy': 0.753394482421875}
store['active_learning_steps'][60]['acquisition']={'indices': [20352, 41868, 17281, 33357, 10344], 'labels': [-1, 5, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8713259696960449})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8502320647239685})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8875804543495178})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9674549102783203})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0461621284484863})
store['active_learning_steps'][61]['training']['best_epoch']=2
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8752, 'crossentropy': 0.81694931640625}
store['active_learning_steps'][61]['acquisition']={'indices': [3234, 52518, 15425, 52497, 27520], 'labels': [1, -1, -1, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8235443830490112})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8320924639701843})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9069876670837402})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.995702862739563})
store['active_learning_steps'][62]['training']['best_epoch']=1
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8587, 'crossentropy': 0.7514474609375}
store['active_learning_steps'][62]['acquisition']={'indices': [19140, 33754, 49670, 13891, 41237], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.842388391494751})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7549517154693604})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8699049353599548})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.928803563117981})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9100863933563232})
store['active_learning_steps'][63]['training']['best_epoch']=2
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8747, 'crossentropy': 0.737705859375}
store['active_learning_steps'][63]['acquisition']={'indices': [37755, 35444, 11051, 16419, 36744], 'labels': [8, 9, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8081285953521729})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8661924600601196})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8891059160232544})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0178983211517334})
store['active_learning_steps'][64]['training']['best_epoch']=1
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8629, 'crossentropy': 0.770054150390625}
store['active_learning_steps'][64]['acquisition']={'indices': [28003, 37091, 46213, 30302, 31199], 'labels': [8, -1, 1, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8047916889190674})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8806601762771606})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8332327604293823})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8972433805465698})
store['active_learning_steps'][65]['training']['best_epoch']=1
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8549, 'crossentropy': 0.78208916015625}
store['active_learning_steps'][65]['acquisition']={'indices': [10565, 58206, 47737, 44964, 43033], 'labels': [1, -1, 5, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8634940981864929})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8070348501205444})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9101612567901611})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8755702972412109})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9324026107788086})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8799, 'crossentropy': 0.7555875}
store['active_learning_steps'][66]['acquisition']={'indices': [42559, 10296, 32822, 22412, 8078], 'labels': [0, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8141471147537231})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7152047157287598})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8292141556739807})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8713244199752808})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9741663932800293})
store['active_learning_steps'][67]['training']['best_epoch']=2
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8883, 'crossentropy': 0.680324169921875}
store['active_learning_steps'][67]['acquisition']={'indices': [9692, 47723, 23755, 7863, 52506], 'labels': [-1, 8, -1, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8700603246688843})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7638391256332397})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8684099912643433})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8980544805526733})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9393243193626404})
store['active_learning_steps'][68]['training']['best_epoch']=2
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8902, 'crossentropy': 0.7127080078125}
store['active_learning_steps'][68]['acquisition']={'indices': [20713, 51269, 22473, 17033, 4438], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8926296830177307})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7578535079956055})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8430013656616211})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9025863409042358})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.934328556060791})
store['active_learning_steps'][69]['training']['best_epoch']=2
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8933, 'crossentropy': 0.710619091796875}
store['active_learning_steps'][69]['acquisition']={'indices': [20491, 4504, 43213, 40659, 34987], 'labels': [8, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7371399998664856})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7009910345077515})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7171833515167236})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.797265887260437})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7643201351165771})
store['active_learning_steps'][70]['training']['best_epoch']=2
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8994, 'crossentropy': 0.65054345703125}
store['active_learning_steps'][70]['acquisition']={'indices': [12239, 20756, 56877, 15172, 15809], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7783238887786865})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7374102473258972})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8154075145721436})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8710163235664368})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9192723035812378})
store['active_learning_steps'][71]['training']['best_epoch']=2
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.881, 'crossentropy': 0.720662890625}
store['active_learning_steps'][71]['acquisition']={'indices': [41663, 39184, 53447, 21067, 488], 'labels': [8, 3, 3, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7811449766159058})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8654955625534058})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8736424446105957})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8855820894241333})
store['active_learning_steps'][72]['training']['best_epoch']=1
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8563, 'crossentropy': 0.76182607421875}
store['active_learning_steps'][72]['acquisition']={'indices': [36292, 25747, 13421, 51001, 58033], 'labels': [2, 5, 7, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7608319520950317})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7522225379943848})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8180235624313354})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8508190512657166})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9133856892585754})
store['active_learning_steps'][73]['training']['best_epoch']=2
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.8866, 'crossentropy': 0.6781599609375}
store['active_learning_steps'][73]['acquisition']={'indices': [3390, 41223, 45978, 31733, 56488], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8392953276634216})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.741752028465271})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7752842903137207})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.837360143661499})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8994199633598328})
store['active_learning_steps'][74]['training']['best_epoch']=2
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.8925, 'crossentropy': 0.640172216796875}
store['active_learning_steps'][74]['acquisition']={'indices': [10537, 13002, 54810, 54487, 25456], 'labels': [-1, -1, 0, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7287658452987671})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.745196521282196})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9494590759277344})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7285915613174438})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8846311569213867})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.951298177242279})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9155502319335938})
store['active_learning_steps'][75]['training']['best_epoch']=4
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9062, 'crossentropy': 0.681864453125}
store['active_learning_steps'][75]['acquisition']={'indices': [35010, 19266, 16431, 1812, 24136], 'labels': [3, 3, 4, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7439095973968506})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7151424288749695})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.805526852607727})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8290897011756897})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.868535041809082})
store['active_learning_steps'][76]['training']['best_epoch']=2
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.8834, 'crossentropy': 0.695152880859375}
store['active_learning_steps'][76]['acquisition']={'indices': [54725, 11776, 53512, 30694, 46877], 'labels': [-1, 5, 2, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8339945077896118})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7444660663604736})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.750089168548584})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8109703063964844})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9301334023475647})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.8919, 'crossentropy': 0.6781251953125}
store['active_learning_steps'][77]['acquisition']={'indices': [55018, 20332, 803, 11506, 32543], 'labels': [-1, 1, 7, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7581048011779785})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.687516450881958})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7463120818138123})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7679817080497742})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7507184147834778})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.8951, 'crossentropy': 0.6426958984375}
store['active_learning_steps'][78]['acquisition']={'indices': [48551, 42770, 55958, 29262, 38837], 'labels': [3, 4, 5, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.828755259513855})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7431861758232117})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6837759017944336})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8477184772491455})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9205529689788818})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8876926898956299})
store['active_learning_steps'][79]['training']['best_epoch']=3
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9061, 'crossentropy': 0.65033935546875}
store['active_learning_steps'][79]['acquisition']={'indices': [52784, 51631, 41123, 24028, 32504], 'labels': [2, 1, 3, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8328648805618286})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6432828307151794})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.724527895450592})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.766946017742157})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7706893682479858})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8965, 'crossentropy': 0.6064494140625}
store['active_learning_steps'][80]['acquisition']={'indices': [47233, 46348, 36066, 28635, 10402], 'labels': [1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.742523193359375})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6949080228805542})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7340278625488281})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8993744254112244})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7980515360832214})
store['active_learning_steps'][81]['training']['best_epoch']=2
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.8935, 'crossentropy': 0.635651171875}
store['active_learning_steps'][81]['acquisition']={'indices': [24490, 19571, 56967, 49938, 48270], 'labels': [-1, 6, -1, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8066293001174927})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.738161563873291})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7631486654281616})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7819370031356812})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7343425154685974})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8414417505264282})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9406616687774658})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8639166355133057})
store['active_learning_steps'][82]['training']['best_epoch']=5
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9092, 'crossentropy': 0.69158251953125}
store['active_learning_steps'][82]['acquisition']={'indices': [12034, 8241, 16937, 18106, 18106], 'labels': [4, 3, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7971040606498718})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7155557870864868})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6879011392593384})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7081917524337769})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7375125288963318})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.79583740234375})
store['active_learning_steps'][83]['training']['best_epoch']=3
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9012, 'crossentropy': 0.6804001953125}
store['active_learning_steps'][83]['acquisition']={'indices': [9417, 47002, 20684, 43956, 31480], 'labels': [6, -1, 9, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7839645147323608})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.724574089050293})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6863726377487183})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6928727626800537})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8167291879653931})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7547169327735901})
store['active_learning_steps'][84]['training']['best_epoch']=3
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9084, 'crossentropy': 0.5896177734375}
store['active_learning_steps'][84]['acquisition']={'indices': [24570, 7982, 19753, 18857, 25113], 'labels': [2, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7416812181472778})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7197874784469604})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7379205226898193})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8594354391098022})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8621399402618408})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.8895, 'crossentropy': 0.644130126953125}
store['active_learning_steps'][85]['acquisition']={'indices': [59830, 26024, 31284, 37828, 8197], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8342680931091309})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7129435539245605})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7056170105934143})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.804581344127655})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7834858894348145})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.757574200630188})
store['active_learning_steps'][86]['training']['best_epoch']=3
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.8989, 'crossentropy': 0.629338818359375}
store['active_learning_steps'][86]['acquisition']={'indices': [35744, 22074, 57889, 15044, 46301], 'labels': [-1, 6, 2, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7666356563568115})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7173963785171509})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8075392246246338})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8109302520751953})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7852734327316284})
store['active_learning_steps'][87]['training']['best_epoch']=2
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.8754, 'crossentropy': 0.712656982421875}
store['active_learning_steps'][87]['acquisition']={'indices': [14988, 40204, 29388, 11439, 12089], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.78743577003479})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6713905334472656})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7152667045593262})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6880714297294617})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7467791438102722})
store['active_learning_steps'][88]['training']['best_epoch']=2
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.8967, 'crossentropy': 0.61887705078125}
store['active_learning_steps'][88]['acquisition']={'indices': [43962, 28966, 14760, 53191, 23919], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8292666673660278})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6752898097038269})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7682072520256042})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7398752570152283})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7873666286468506})
store['active_learning_steps'][89]['training']['best_epoch']=2
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.8882, 'crossentropy': 0.632236376953125}
store['active_learning_steps'][89]['acquisition']={'indices': [34625, 15188, 39920, 13317, 25260], 'labels': [-1, 6, -1, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8422911167144775})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6893148422241211})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.713881254196167})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7003076672554016})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8478176593780518})
store['active_learning_steps'][90]['training']['best_epoch']=2
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.8859, 'crossentropy': 0.660818115234375}
store['active_learning_steps'][90]['acquisition']={'indices': [58904, 23610, 59056, 16557, 38360], 'labels': [6, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8201177716255188})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.633784294128418})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6245467066764832})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7033920288085938})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8481981158256531})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7818214893341064})
store['active_learning_steps'][91]['training']['best_epoch']=3
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9061, 'crossentropy': 0.60671474609375}
store['active_learning_steps'][91]['acquisition']={'indices': [41021, 26825, 38559, 39802, 40737], 'labels': [-1, -1, 0, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6753745079040527})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.693247377872467})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.650913655757904})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7497309446334839})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7114749550819397})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.796362042427063})
store['active_learning_steps'][92]['training']['best_epoch']=3
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.906, 'crossentropy': 0.5987947265625}
store['active_learning_steps'][92]['acquisition']={'indices': [40779, 29671, 36652, 27239, 19224], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7256475687026978})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.754744291305542})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7221416234970093})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.824053168296814})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8355482816696167})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.915086030960083})
store['active_learning_steps'][93]['training']['best_epoch']=3
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.8964, 'crossentropy': 0.675922607421875}
store['active_learning_steps'][93]['acquisition']={'indices': [43295, 50291, 41431, 51816, 6928], 'labels': [4, 0, 8, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7380285263061523})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6388479471206665})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6606581211090088})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7043865919113159})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.791576623916626})
store['active_learning_steps'][94]['training']['best_epoch']=2
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.8948, 'crossentropy': 0.6026544921875}
store['active_learning_steps'][94]['acquisition']={'indices': [14738, 56151, 38546, 20206, 32618], 'labels': [3, 8, -1, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.725674033164978})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6357743740081787})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5827336311340332})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.594341516494751})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7343461513519287})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7342698574066162})
store['active_learning_steps'][95]['training']['best_epoch']=3
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9073, 'crossentropy': 0.555531494140625}
store['active_learning_steps'][95]['acquisition']={'indices': [17529, 12030, 26941, 29368, 47860], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.712425708770752})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6401020884513855})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.654665470123291})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6044565439224243})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6997177004814148})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6996084451675415})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.733473002910614})
store['active_learning_steps'][96]['training']['best_epoch']=4
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9126, 'crossentropy': 0.59239716796875}
store['active_learning_steps'][96]['acquisition']={'indices': [6051, 48906, 32079, 3557, 12661], 'labels': [9, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7631679773330688})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6706452369689941})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6965052485466003})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7871140241622925})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.800316572189331})
store['active_learning_steps'][97]['training']['best_epoch']=2
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.8904, 'crossentropy': 0.628618896484375}
store['active_learning_steps'][97]['acquisition']={'indices': [12085, 21157, 27445, 45160, 19238], 'labels': [8, -1, 0, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7760306596755981})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6585948467254639})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6817926168441772})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7729584574699402})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7967934608459473})
store['active_learning_steps'][98]['training']['best_epoch']=2
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.8981, 'crossentropy': 0.60611630859375}
store['active_learning_steps'][98]['acquisition']={'indices': [26918, 26945, 20155, 19415, 21619], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7329341173171997})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6353907585144043})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6312251091003418})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7227808237075806})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.696908712387085})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7548995018005371})
store['active_learning_steps'][99]['training']['best_epoch']=3
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9134, 'crossentropy': 0.552084375}
store['active_learning_steps'][99]['acquisition']={'indices': [13183, 24774, 19558, 45488, 32970], 'labels': [4, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7259736061096191})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6503667831420898})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7335537672042847})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7525732517242432})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7833678722381592})
store['active_learning_steps'][100]['training']['best_epoch']=2
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9052, 'crossentropy': 0.582530517578125}
store['active_learning_steps'][100]['acquisition']={'indices': [53460, 36870, 19682, 8053, 7017], 'labels': [0, 8, 0, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7296026945114136})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6381822824478149})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7097145915031433})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6479910612106323})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7347530722618103})
store['active_learning_steps'][101]['training']['best_epoch']=2
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9052, 'crossentropy': 0.590941357421875}
store['active_learning_steps'][101]['acquisition']={'indices': [23187, 59407, 22661, 31604, 56763], 'labels': [-1, -1, 2, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6814050674438477})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6085027456283569})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6992958784103394})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5967457294464111})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7437766790390015})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6355654001235962})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6424683332443237})
store['active_learning_steps'][102]['training']['best_epoch']=4
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.554837451171875}
store['active_learning_steps'][102]['acquisition']={'indices': [57592, 42837, 56893, 46469, 58562], 'labels': [-1, 1, 4, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7067188024520874})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6643794775009155})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7297083139419556})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.744430422782898})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7419041991233826})
store['active_learning_steps'][103]['training']['best_epoch']=2
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.89, 'crossentropy': 0.635227587890625}
store['active_learning_steps'][103]['acquisition']={'indices': [12921, 26700, 56397, 4293, 13534], 'labels': [7, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6515748500823975})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.55277419090271})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6037808656692505})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6304806470870972})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5816431045532227})
store['active_learning_steps'][104]['training']['best_epoch']=2
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.912, 'crossentropy': 0.53257900390625}
store['active_learning_steps'][104]['acquisition']={'indices': [11055, 8469, 29587, 44070, 58206], 'labels': [-1, 0, 1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8017588257789612})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6812974810600281})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7564584016799927})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7072595357894897})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7349315285682678})
store['active_learning_steps'][105]['training']['best_epoch']=2
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.8864, 'crossentropy': 0.672417529296875}
store['active_learning_steps'][105]['acquisition']={'indices': [6892, 56476, 49513, 37902, 27874], 'labels': [-1, 5, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8375195264816284})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5876182317733765})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6571643352508545})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6848151683807373})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7703218460083008})
store['active_learning_steps'][106]['training']['best_epoch']=2
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9024, 'crossentropy': 0.57323291015625}
store['active_learning_steps'][106]['acquisition']={'indices': [46179, 31128, 41048, 42186, 57045], 'labels': [9, -1, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7755305767059326})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7047584056854248})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6771560311317444})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6634719371795654})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.772354006767273})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7445238828659058})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6793011426925659})
store['active_learning_steps'][107]['training']['best_epoch']=4
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9134, 'crossentropy': 0.586421923828125}
store['active_learning_steps'][107]['acquisition']={'indices': [22760, 6463, 21827, 24757, 30580], 'labels': [8, 1, 9, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7781124711036682})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6709467768669128})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6146291494369507})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7266469597816467})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6738988757133484})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.746068000793457})
store['active_learning_steps'][108]['training']['best_epoch']=3
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9119, 'crossentropy': 0.572368212890625}
store['active_learning_steps'][108]['acquisition']={'indices': [23729, 12835, 54284, 38899, 904], 'labels': [-1, 7, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7352591753005981})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6035616397857666})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6431519985198975})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6073958277702332})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6307802200317383})
store['active_learning_steps'][109]['training']['best_epoch']=2
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.8987, 'crossentropy': 0.589064990234375}
store['active_learning_steps'][109]['acquisition']={'indices': [35361, 30628, 26799, 40700, 4020], 'labels': [7, -1, 0, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.754860520362854})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6269620060920715})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6368085145950317})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7382959127426147})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7074481248855591})
store['active_learning_steps'][110]['training']['best_epoch']=2
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9009, 'crossentropy': 0.576510888671875}
store['active_learning_steps'][110]['acquisition']={'indices': [19568, 23475, 15113, 3581, 36266], 'labels': [-1, 6, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7257163524627686})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5574883818626404})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6080666780471802})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7105132341384888})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6618030071258545})
store['active_learning_steps'][111]['training']['best_epoch']=2
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.539709375}
store['active_learning_steps'][111]['acquisition']={'indices': [46234, 16295, 31709, 22867, 16285], 'labels': [-1, 5, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7170754671096802})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6140410900115967})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.690537691116333})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.638630747795105})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6293339729309082})
store['active_learning_steps'][112]['training']['best_epoch']=2
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9077, 'crossentropy': 0.56676357421875}
store['active_learning_steps'][112]['acquisition']={'indices': [48045, 39912, 3454, 15571, 12611], 'labels': [-1, -1, 6, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6544144153594971})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5948243141174316})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6933349370956421})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6591159105300903})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6451391577720642})
store['active_learning_steps'][113]['training']['best_epoch']=2
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.548784765625}
store['active_learning_steps'][113]['acquisition']={'indices': [45505, 16462, 6358, 11101, 45222], 'labels': [2, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7499016523361206})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5960140228271484})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6481219530105591})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5836104154586792})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6106662750244141})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6404401063919067})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6648387908935547})
store['active_learning_steps'][114]['training']['best_epoch']=4
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.567377685546875}
store['active_learning_steps'][114]['acquisition']={'indices': [47425, 50254, 35896, 2712, 17502], 'labels': [-1, 7, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6786067485809326})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6571223139762878})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6261208057403564})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.679430365562439})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6502536535263062})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6486586332321167})
store['active_learning_steps'][115]['training']['best_epoch']=3
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.52987099609375}
store['active_learning_steps'][115]['acquisition']={'indices': [58160, 25481, 30388, 54246, 53982], 'labels': [0, 7, 0, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.765780508518219})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5961587429046631})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6534315943717957})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6155170202255249})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6857509613037109})
store['active_learning_steps'][116]['training']['best_epoch']=2
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9004, 'crossentropy': 0.595606982421875}
store['active_learning_steps'][116]['acquisition']={'indices': [3519, 2605, 13630, 18991, 292], 'labels': [-1, -1, 1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6590187549591064})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6289874911308289})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.621596097946167})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.657451868057251})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6517437100410461})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6703121662139893})
store['active_learning_steps'][117]['training']['best_epoch']=3
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9143, 'crossentropy': 0.5690412109375}
store['active_learning_steps'][117]['acquisition']={'indices': [27193, 49765, 43730, 19115, 49948], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6913005113601685})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5616286993026733})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6680848598480225})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6438145637512207})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6657679677009583})
store['active_learning_steps'][118]['training']['best_epoch']=2
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9039, 'crossentropy': 0.561269384765625}
store['active_learning_steps'][118]['acquisition']={'indices': [48241, 43264, 34864, 4326, 38577], 'labels': [-1, 6, 2, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6912473440170288})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5757434368133545})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5640153884887695})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6406762599945068})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.642059326171875})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6567655801773071})
store['active_learning_steps'][119]['training']['best_epoch']=3
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.9131, 'crossentropy': 0.544738818359375}
store['active_learning_steps'][119]['acquisition']={'indices': [2069, 17959, 24954, 42973, 25069], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7184699773788452})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6108610033988953})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.627646803855896})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5916270017623901})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6245464086532593})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.667769193649292})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6716911792755127})
store['active_learning_steps'][120]['training']['best_epoch']=4
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.56137783203125}
store['active_learning_steps'][120]['acquisition']={'indices': [2764, 14244, 50413, 43523, 30375], 'labels': [9, -1, 8, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.700079083442688})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5658031702041626})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5410774946212769})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.612972617149353})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6495606899261475})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6031248569488525})
store['active_learning_steps'][121]['training']['best_epoch']=3
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9108, 'crossentropy': 0.540208056640625}
store['active_learning_steps'][121]['acquisition']={'indices': [128, 26780, 34259, 6292, 12051], 'labels': [1, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7295674085617065})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6326762437820435})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6127475500106812})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6433883905410767})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6406829357147217})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7464914321899414})
store['active_learning_steps'][122]['training']['best_epoch']=3
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9137, 'crossentropy': 0.54056845703125}
store['active_learning_steps'][122]['acquisition']={'indices': [58575, 528, 15080, 38288, 45682], 'labels': [0, 8, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6522050499916077})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6550350785255432})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6166723966598511})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6053138971328735})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6670480966567993})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6594625115394592})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7541437149047852})
store['active_learning_steps'][123]['training']['best_epoch']=4
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.534777490234375}
store['active_learning_steps'][123]['acquisition']={'indices': [58556, 34172, 41421, 14209, 56519], 'labels': [8, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7562002539634705})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.588631272315979})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6031193733215332})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5557665824890137})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6256200671195984})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6567035913467407})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6223801374435425})
store['active_learning_steps'][124]['training']['best_epoch']=4
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9232, 'crossentropy': 0.50378935546875}
store['active_learning_steps'][124]['acquisition']={'indices': [9323, 32917, 42438, 28816, 22385], 'labels': [-1, -1, 9, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6502034068107605})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5543040037155151})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.568377673625946})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5441054701805115})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5851442813873291})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6530848741531372})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6970803737640381})
store['active_learning_steps'][125]['training']['best_epoch']=4
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9229, 'crossentropy': 0.5327583984375}
store['active_learning_steps'][125]['acquisition']={'indices': [40325, 40325, 32635, 41150, 40615], 'labels': [9, -1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7162550091743469})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6259191632270813})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5950162410736084})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6725046634674072})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6433267593383789})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6296753883361816})
store['active_learning_steps'][126]['training']['best_epoch']=3
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.55701787109375}
store['active_learning_steps'][126]['acquisition']={'indices': [39629, 19255, 36650, 34495, 29413], 'labels': [-1, 9, 7, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7576650977134705})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6740909814834595})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.691512942314148})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6295957565307617})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6483910083770752})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6697445511817932})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7035198211669922})
store['active_learning_steps'][127]['training']['best_epoch']=4
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9149, 'crossentropy': 0.547226708984375}
store['active_learning_steps'][127]['acquisition']={'indices': [1580, 17375, 12110, 23605, 40845], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6500253677368164})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6633013486862183})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6317135691642761})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6899767518043518})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6330809593200684})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6995216608047485})
store['active_learning_steps'][128]['training']['best_epoch']=3
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9088, 'crossentropy': 0.56004228515625}
store['active_learning_steps'][128]['acquisition']={'indices': [52398, 19453, 43209, 54411, 21428], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6426033973693848})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5224186182022095})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6213714480400085})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5792719125747681})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6644187569618225})
store['active_learning_steps'][129]['training']['best_epoch']=2
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9162, 'crossentropy': 0.4974712890625}
store['active_learning_steps'][129]['acquisition']={'indices': [40359, 20612, 16311, 1019, 42106], 'labels': [1, 2, 3, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.714467465877533})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5984059572219849})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6088771820068359})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7077836394309998})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.654704213142395})
store['active_learning_steps'][130]['training']['best_epoch']=2
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9037, 'crossentropy': 0.553812353515625}
store['active_learning_steps'][130]['acquisition']={'indices': [34064, 16758, 31592, 14322, 58986], 'labels': [-1, 0, -1, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7174374461174011})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6248747110366821})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5904414653778076})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5729327201843262})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5985292792320251})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6654510498046875})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6634550094604492})
store['active_learning_steps'][131]['training']['best_epoch']=4
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9199, 'crossentropy': 0.5148177734375}
store['active_learning_steps'][131]['acquisition']={'indices': [31320, 59249, 13704, 41980, 49773], 'labels': [-1, -1, 3, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7175333499908447})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6630111932754517})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6080799102783203})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5974907875061035})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.591396689414978})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5837252736091614})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7128846645355225})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6520191431045532})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6914435029029846})
store['active_learning_steps'][132]['training']['best_epoch']=6
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9228, 'crossentropy': 0.55166025390625}
store['active_learning_steps'][132]['acquisition']={'indices': [18230, 9254, 43780, 38305, 52187], 'labels': [2, -1, 5, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6904771327972412})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6173243522644043})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6269636154174805})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6330245733261108})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6756771802902222})
store['active_learning_steps'][133]['training']['best_epoch']=2
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9042, 'crossentropy': 0.582731982421875}
store['active_learning_steps'][133]['acquisition']={'indices': [15547, 11412, 8124, 49210, 35384], 'labels': [-1, 1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6581482887268066})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.49756455421447754})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6315701007843018})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5508559942245483})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5931466817855835})
store['active_learning_steps'][134]['training']['best_epoch']=2
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.911, 'crossentropy': 0.502125244140625}
store['active_learning_steps'][134]['acquisition']={'indices': [3995, 47025, 58542, 2745, 12717], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.720878005027771})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6113893985748291})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.608415961265564})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.687512993812561})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6790395975112915})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6648093461990356})
store['active_learning_steps'][135]['training']['best_epoch']=3
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9072, 'crossentropy': 0.5704365234375}
store['active_learning_steps'][135]['acquisition']={'indices': [53096, 25225, 970, 605, 3174], 'labels': [5, 3, 5, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6975412368774414})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5184178948402405})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6014353036880493})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5987111330032349})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6601927280426025})
store['active_learning_steps'][136]['training']['best_epoch']=2
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9227, 'crossentropy': 0.47397705078125}
store['active_learning_steps'][136]['acquisition']={'indices': [49725, 1035, 12117, 39381, 27139], 'labels': [3, 3, 3, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7685022354125977})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5862655639648438})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5644371509552002})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5866475105285645})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5950050354003906})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6456553936004639})
store['active_learning_steps'][137]['training']['best_epoch']=3
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.535050390625}
store['active_learning_steps'][137]['acquisition']={'indices': [46896, 6250, 26477, 7503, 7904], 'labels': [0, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7320055961608887})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6144005060195923})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6070085167884827})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5853565335273743})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6219300031661987})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6601101160049438})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7042710781097412})
store['active_learning_steps'][138]['training']['best_epoch']=4
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.92, 'crossentropy': 0.51739443359375}
store['active_learning_steps'][138]['acquisition']={'indices': [45566, 3064, 11495, 11663, 54602], 'labels': [-1, 2, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6760109663009644})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6021963357925415})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5484292507171631})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6101428866386414})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6067911386489868})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6028635501861572})
store['active_learning_steps'][139]['training']['best_epoch']=3
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.50559296875}
store['active_learning_steps'][139]['acquisition']={'indices': [37196, 37018, 59895, 25682, 49895], 'labels': [1, -1, 6, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7015024423599243})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5935455560684204})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5761817693710327})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6360611915588379})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.618024468421936})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6432791948318481})
store['active_learning_steps'][140]['training']['best_epoch']=3
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.53051796875}
store['active_learning_steps'][140]['acquisition']={'indices': [14445, 28405, 47186, 48453, 17211], 'labels': [-1, -1, 0, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.673670768737793})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5975238084793091})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5719499588012695})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5904549360275269})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5705999135971069})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6484693884849548})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5699100494384766})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6181718707084656})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6418966054916382})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6797055006027222})
store['active_learning_steps'][141]['training']['best_epoch']=7
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.5162009765625}
store['active_learning_steps'][141]['acquisition']={'indices': [4414, 10011, 59762, 32205, 20607], 'labels': [2, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7177387475967407})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6289942264556885})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.624427318572998})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5744876861572266})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.630350649356842})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6594937443733215})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6363950967788696})
store['active_learning_steps'][142]['training']['best_epoch']=4
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9171, 'crossentropy': 0.52908486328125}
store['active_learning_steps'][142]['acquisition']={'indices': [915, 15511, 49370, 41503, 30364], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.696062445640564})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.594858705997467})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6076381802558899})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6102132797241211})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.556567907333374})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6625844240188599})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.609889566898346})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5735300779342651})
store['active_learning_steps'][143]['training']['best_epoch']=5
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.5634892578125}
store['active_learning_steps'][143]['acquisition']={'indices': [26878, 1570, 38581, 16049, 22273], 'labels': [-1, 7, 8, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7423930168151855})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6148542165756226})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6035856604576111})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5657123923301697})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5705692768096924})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6531903743743896})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6825733184814453})
store['active_learning_steps'][144]['training']['best_epoch']=4
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9259, 'crossentropy': 0.510370166015625}
store['active_learning_steps'][144]['acquisition']={'indices': [30823, 21043, 29383, 54212, 57900], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6924338936805725})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6200662851333618})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5296797752380371})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6391664743423462})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5463826656341553})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6510237455368042})
store['active_learning_steps'][145]['training']['best_epoch']=3
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9256, 'crossentropy': 0.476324609375}
store['active_learning_steps'][145]['acquisition']={'indices': [58503, 30852, 29576, 44928, 9378], 'labels': [-1, 1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7222990989685059})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6044977903366089})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5074270963668823})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5689946413040161})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5994322299957275})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5459176898002625})
store['active_learning_steps'][146]['training']['best_epoch']=3
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.9261, 'crossentropy': 0.465408203125}
store['active_learning_steps'][146]['acquisition']={'indices': [11715, 20935, 58912, 16635, 35358], 'labels': [1, -1, 7, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6985273361206055})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6210048198699951})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5047587156295776})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.535476803779602})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5352878570556641})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5994936227798462})
store['active_learning_steps'][147]['training']['best_epoch']=3
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9201, 'crossentropy': 0.484962353515625}
store['active_learning_steps'][147]['acquisition']={'indices': [13426, 34759, 42044, 44886, 23768], 'labels': [4, -1, 1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6276165843009949})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5262068510055542})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5011380314826965})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5309081673622131})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5629525780677795})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5719901323318481})
store['active_learning_steps'][148]['training']['best_epoch']=3
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.469378759765625}
store['active_learning_steps'][148]['acquisition']={'indices': [9964, 43367, 1898, 16024, 58077], 'labels': [-1, -1, 6, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7312523126602173})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6264486312866211})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6078557968139648})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5244619846343994})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6361390352249146})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6306113004684448})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5519102811813354})
store['active_learning_steps'][149]['training']['best_epoch']=4
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9232, 'crossentropy': 0.500428173828125}
store['active_learning_steps'][149]['acquisition']={'indices': [29133, 48289, 29609, 33119, 36621], 'labels': [1, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7134671807289124})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5990961194038391})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5775986909866333})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6002771854400635})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5848491191864014})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5630332231521606})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.583364725112915})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.573027491569519})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6890550851821899})
store['active_learning_steps'][150]['training']['best_epoch']=6
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9312, 'crossentropy': 0.50689912109375}
store['active_learning_steps'][150]['acquisition']={'indices': [22481, 1632, 15494, 19928, 44319], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6950478553771973})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5761120915412903})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.61176997423172})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6502004861831665})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6325758695602417})
store['active_learning_steps'][151]['training']['best_epoch']=2
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9082, 'crossentropy': 0.5358888671875}
store['active_learning_steps'][151]['acquisition']={'indices': [9858, 23123, 49797, 31867, 16950], 'labels': [5, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7213774919509888})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5310370922088623})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5286297798156738})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5425131916999817})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5336354970932007})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.543677806854248})
store['active_learning_steps'][152]['training']['best_epoch']=3
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9187, 'crossentropy': 0.48517685546875}
store['active_learning_steps'][152]['acquisition']={'indices': [58350, 11277, 23620, 7081, 13607], 'labels': [-1, -1, 5, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7356547117233276})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.584120512008667})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.564365565776825})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5734199285507202})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5902653932571411})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5481388568878174})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5479156970977783})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.65342116355896})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5725295543670654})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5887936353683472})
store['active_learning_steps'][153]['training']['best_epoch']=7
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9318, 'crossentropy': 0.5282390625}
store['active_learning_steps'][153]['acquisition']={'indices': [10701, 52312, 20996, 12829, 48133], 'labels': [-1, 0, 7, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7509920597076416})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6236447095870972})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6140965223312378})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6065433621406555})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6161732077598572})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6138865947723389})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5785936117172241})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6921303272247314})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7211438417434692})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6086360216140747})
store['active_learning_steps'][154]['training']['best_epoch']=7
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9251, 'crossentropy': 0.535840185546875}
store['active_learning_steps'][154]['acquisition']={'indices': [24558, 52971, 42297, 29952, 1366], 'labels': [8, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7662531137466431})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5656362771987915})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6046054363250732})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5043678879737854})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6105121374130249})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6091374158859253})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5663308501243591})
store['active_learning_steps'][155]['training']['best_epoch']=4
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9237, 'crossentropy': 0.48501630859375}
store['active_learning_steps'][155]['acquisition']={'indices': [14866, 3430, 35574, 10537, 32604], 'labels': [7, 1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6599702835083008})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5790922045707703})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5481621026992798})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5666157007217407})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6024439334869385})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6677600145339966})
store['active_learning_steps'][156]['training']['best_epoch']=3
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9254, 'crossentropy': 0.480285205078125}
store['active_learning_steps'][156]['acquisition']={'indices': [47735, 3936, 16865, 33054, 18884], 'labels': [1, 6, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7452194690704346})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5683039426803589})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6286145448684692})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5924777984619141})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6427823305130005})
store['active_learning_steps'][157]['training']['best_epoch']=2
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9121, 'crossentropy': 0.528331689453125}
store['active_learning_steps'][157]['acquisition']={'indices': [50242, 830, 50240, 40411, 41716], 'labels': [-1, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6626690626144409})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5977534055709839})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5418721437454224})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5894277095794678})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.573415994644165})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6491689682006836})
store['active_learning_steps'][158]['training']['best_epoch']=3
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9185, 'crossentropy': 0.479092724609375}
store['active_learning_steps'][158]['acquisition']={'indices': [21446, 32847, 45526, 46859, 11769], 'labels': [1, 3, -1, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.696872353553772})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.599433422088623})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5628810524940491})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5580041408538818})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5490526556968689})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6098408699035645})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5831199884414673})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6435754299163818})
store['active_learning_steps'][159]['training']['best_epoch']=5
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9334, 'crossentropy': 0.471978515625}
store['active_learning_steps'][159]['acquisition']={'indices': [58335, 46632, 40846, 44156, 36770], 'labels': [1, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6702821254730225})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5761377215385437})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5645771026611328})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5995954275131226})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6022546291351318})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6397556066513062})
store['active_learning_steps'][160]['training']['best_epoch']=3
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.51528720703125}
store['active_learning_steps'][160]['acquisition']={'indices': [9498, 53384, 56814, 42804, 17711], 'labels': [-1, 4, 7, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7639361023902893})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5822826623916626})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5602654218673706})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5889768600463867})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6111998558044434})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5526649355888367})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5733355283737183})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6211163401603699})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5734076499938965})
store['active_learning_steps'][161]['training']['best_epoch']=6
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.506725}
store['active_learning_steps'][161]['acquisition']={'indices': [34882, 11547, 37078, 53604, 37482], 'labels': [-1, -1, 8, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6538286209106445})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5587838888168335})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5508201122283936})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5294539928436279})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5479687452316284})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5990726947784424})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.545335054397583})
store['active_learning_steps'][162]['training']['best_epoch']=4
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9283, 'crossentropy': 0.4674578125}
store['active_learning_steps'][162]['acquisition']={'indices': [1383, 10975, 22985, 39146, 57119], 'labels': [-1, 0, 4, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7289526462554932})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5895972847938538})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6077814102172852})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5738347172737122})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6087459921836853})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5652515888214111})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6600239276885986})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6534233093261719})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6717466115951538})
store['active_learning_steps'][163]['training']['best_epoch']=6
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9246, 'crossentropy': 0.50867685546875}
store['active_learning_steps'][163]['acquisition']={'indices': [12024, 4200, 57531, 29581, 57037], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6553504467010498})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5936093330383301})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5490921139717102})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5319235324859619})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5674914121627808})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.583808422088623})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.661704421043396})
store['active_learning_steps'][164]['training']['best_epoch']=4
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9227, 'crossentropy': 0.473240380859375}
store['active_learning_steps'][164]['acquisition']={'indices': [33446, 10989, 23823, 30851, 11372], 'labels': [1, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7151526212692261})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5355055332183838})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5659257173538208})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5082046389579773})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5812821388244629})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6068955063819885})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5579644441604614})
store['active_learning_steps'][165]['training']['best_epoch']=4
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9298, 'crossentropy': 0.4513103515625}
store['active_learning_steps'][165]['acquisition']={'indices': [21185, 25079, 48591, 50649, 50845], 'labels': [6, 7, 6, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6606324315071106})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.525078535079956})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5050840377807617})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.552997350692749})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5368297100067139})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5512365102767944})
store['active_learning_steps'][166]['training']['best_epoch']=3
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.9265, 'crossentropy': 0.452514453125}
store['active_learning_steps'][166]['acquisition']={'indices': [52216, 13684, 53422, 40511, 9877], 'labels': [-1, 7, 6, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7758641242980957})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5564136505126953})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5688027143478394})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.595562219619751})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5327692031860352})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6336157917976379})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5373544692993164})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5899351835250854})
store['active_learning_steps'][167]['training']['best_epoch']=5
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.929, 'crossentropy': 0.476647021484375}
store['active_learning_steps'][167]['acquisition']={'indices': [49128, 1206, 30855, 54421, 2367], 'labels': [-1, -1, 6, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7313232421875})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5717111825942993})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.585085391998291})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.580114483833313})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5700239539146423})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6451700925827026})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.624934196472168})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6847966909408569})
store['active_learning_steps'][168]['training']['best_epoch']=5
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9274, 'crossentropy': 0.4843677734375}
store['active_learning_steps'][168]['acquisition']={'indices': [42699, 28129, 57554, 4363, 35175], 'labels': [8, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][169]['training']={}
store['active_learning_steps'][169]['training']['epochs']=[]
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6552397608757019})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5049295425415039})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5108150839805603})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5658119916915894})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5691868662834167})
store['active_learning_steps'][169]['training']['best_epoch']=2
store['active_learning_steps'][169]['evaluation_metrics']={'accuracy': 0.9209, 'crossentropy': 0.477199072265625}
store['active_learning_steps'][169]['acquisition']={'indices': [48377, 5367, 50849, 8384, 29754], 'labels': [7, -1, 7, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][170]['training']={}
store['active_learning_steps'][170]['training']['epochs']=[]
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6753001809120178})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5404794216156006})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5594865083694458})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6218830347061157})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5301903486251831})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6020750999450684})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5213738679885864})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6355583071708679})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6475684642791748})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6144975423812866})
store['active_learning_steps'][170]['training']['best_epoch']=7
store['active_learning_steps'][170]['evaluation_metrics']={'accuracy': 0.9385, 'crossentropy': 0.444557421875}
store['active_learning_steps'][170]['acquisition']={'indices': [51950, 37610, 47569, 7088, 50909], 'labels': [-1, -1, 4, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][171]['training']={}
store['active_learning_steps'][171]['training']['epochs']=[]
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7019293904304504})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5369713306427002})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5284521579742432})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5400398969650269})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5272274613380432})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6200222969055176})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.556444525718689})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6694095134735107})
store['active_learning_steps'][171]['training']['best_epoch']=5
store['active_learning_steps'][171]['evaluation_metrics']={'accuracy': 0.9294, 'crossentropy': 0.473571533203125}
store['active_learning_steps'][171]['acquisition']={'indices': [33316, 26099, 27166, 32365, 16048], 'labels': [3, 1, 7, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][172]['training']={}
store['active_learning_steps'][172]['training']['epochs']=[]
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6951358914375305})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5437034368515015})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5436854958534241})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5570616722106934})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6034003496170044})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.611752986907959})
store['active_learning_steps'][172]['training']['best_epoch']=3
store['active_learning_steps'][172]['evaluation_metrics']={'accuracy': 0.9154, 'crossentropy': 0.5036794921875}
store['active_learning_steps'][172]['acquisition']={'indices': [5392, 55240, 4888, 43108, 52273], 'labels': [-1, 9, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][173]['training']={}
store['active_learning_steps'][173]['training']['epochs']=[]
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6501392126083374})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5659611821174622})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.508036732673645})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5715700387954712})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6013146638870239})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5435498356819153})
store['active_learning_steps'][173]['training']['best_epoch']=3
store['active_learning_steps'][173]['evaluation_metrics']={'accuracy': 0.9218, 'crossentropy': 0.470821044921875}
store['active_learning_steps'][173]['acquisition']={'indices': [9948, 25827, 6465, 3715, 20711], 'labels': [8, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][174]['training']={}
store['active_learning_steps'][174]['training']['epochs']=[]
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6897013187408447})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5578048825263977})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5192875862121582})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5179988145828247})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5290393829345703})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5353987216949463})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5527768135070801})
store['active_learning_steps'][174]['training']['best_epoch']=4
store['active_learning_steps'][174]['evaluation_metrics']={'accuracy': 0.9253, 'crossentropy': 0.4728947265625}
store['active_learning_steps'][174]['acquisition']={'indices': [56496, 40849, 7891, 12716, 30383], 'labels': [-1, -1, 8, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][175]['training']={}
store['active_learning_steps'][175]['training']['epochs']=[]
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6797947287559509})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5755624175071716})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5735634565353394})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5684470534324646})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5203882455825806})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5330941677093506})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5947180390357971})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5593137741088867})
store['active_learning_steps'][175]['training']['best_epoch']=5
store['active_learning_steps'][175]['evaluation_metrics']={'accuracy': 0.9293, 'crossentropy': 0.468363134765625}
store['active_learning_steps'][175]['acquisition']={'indices': [24747, 19034, 14060, 17231, 38958], 'labels': [3, 4, 1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][176]['training']={}
store['active_learning_steps'][176]['training']['epochs']=[]
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6540720462799072})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4955827593803406})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5220576524734497})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.44636261463165283})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.503287672996521})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.48815029859542847})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5176058411598206})
store['active_learning_steps'][176]['training']['best_epoch']=4
store['active_learning_steps'][176]['evaluation_metrics']={'accuracy': 0.937, 'crossentropy': 0.415176806640625}
store['active_learning_steps'][176]['acquisition']={'indices': [4803, 15731, 34539, 24611, 14985], 'labels': [8, -1, 6, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][177]['training']={}
store['active_learning_steps'][177]['training']['epochs']=[]
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7359250783920288})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.531697154045105})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5214658379554749})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5143928527832031})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5670415163040161})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5755975246429443})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6319295167922974})
store['active_learning_steps'][177]['training']['best_epoch']=4
store['active_learning_steps'][177]['evaluation_metrics']={'accuracy': 0.9265, 'crossentropy': 0.459067431640625}
