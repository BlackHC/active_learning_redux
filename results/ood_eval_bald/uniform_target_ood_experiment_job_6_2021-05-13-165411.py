store = {}
store['timestamp']=1620921251
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=6']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=6
store['worker_id']=6
store['num_workers']=20
store['config']={'seed': 1243, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.247647285461426})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.764303684234619})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5868282318115234})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.9454288482666016})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6869, 'crossentropy': 2.0332689453125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.15549635887146})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.080956220626831})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1798160076141357})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 17671], ['id', 9936], ['id', 45509], ['id', 42580], ['id', 59282], ['id', 37803], ['ood', 49237], ['id', 14935], ['id', 20048], ['id', 30782]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.8915632367134094, 0.7332107424736023, 0.6740407943725586, 0.9007425308227539, 0.6366531848907471, 0.809978187084198, 0.5717312097549438, 0.7036681771278381, 0.5747951865196228, 1.033774971961975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.5150785446166992})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.8948462009429932})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.99062180519104})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.4247212409973145})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7395, 'crossentropy': 1.413655078125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.104636311531067})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9542981386184692})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.959101676940918})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 26873], ['id', 31485], ['id', 34391], ['id', 10961], ['id', 58831], ['id', 20629], ['id', 14078], ['id', 21932], ['id', 52095], ['id', 30439]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6214016675949097, 0.5494406819343567, 0.6206802129745483, 0.4788799285888672, 0.679389476776123, 0.4456007778644562, 0.5067903399467468, 0.5023554563522339, 0.49161744117736816, 0.6651479601860046]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.6240594387054443})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.8005386590957642})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.9756028652191162})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.9902230501174927})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7441, 'crossentropy': 1.34858798828125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9732382893562317})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9729845523834229})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9909088015556335})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 5265], ['id', 57470], ['id', 12443], ['id', 5897], ['id', 50633], ['id', 32971], ['id', 4915], ['id', 29381], ['ood', 45660], ['id', 6348]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5436415672302246, 0.5984051823616028, 0.4943327307701111, 0.6067056059837341, 0.5073732137680054, 0.4067338705062866, 0.3883104920387268, 0.4233567714691162, 0.43660664558410645, 0.5230008363723755]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0389280319213867})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.14314866065979})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.1536126136779785})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.2935783863067627})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.822, 'crossentropy': 0.9277314453125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8859613537788391})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.7605690956115723})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.7526916861534119})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 24278], ['id', 33210], ['id', 15423], ['id', 291], ['id', 36602], ['id', 50734], ['id', 39662], ['id', 29753], ['id', 1579], ['id', 14893]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.42540526390075684, 0.405825138092041, 0.48465538024902344, 0.4573711156845093, 0.40129613876342773, 0.3858736753463745, 0.557367742061615, 0.4537314176559448, 0.4341011643409729, 0.4513171911239624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9199401140213013})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9521108865737915})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9801733493804932})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0272560119628906})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.843, 'crossentropy': 0.8359375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8508221507072449})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7488651275634766})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7600187063217163})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 29352], ['id', 31252], ['id', 42070], ['id', 49060], ['id', 42165], ['id', 3322], ['id', 1023], ['id', 28319], ['id', 34303], ['id', 17218]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.2810938358306885, 0.4976435899734497, 0.3878963589668274, 0.5022402405738831, 0.42049551010131836, 0.4241253137588501, 0.4651678800582886, 0.43872880935668945, 0.42389631271362305, 0.28375792503356934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9170359373092651})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7985403537750244})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8012912273406982})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8902607560157776})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8647297620773315})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8807, 'crossentropy': 0.722365283203125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7263761758804321})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6403694152832031})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5812290906906128})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5812610387802124})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 57725], ['id', 13720], ['id', 34468], ['id', 52861], ['id', 37005], ['id', 43052], ['id', 16210], ['id', 41499], ['id', 53758], ['id', 49493]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4545620083808899, 0.5079113245010376, 0.3449861407279968, 0.38721907138824463, 0.4186025857925415, 0.5339519679546356, 0.4428233504295349, 0.46376514434814453, 0.4999741315841675, 0.527702808380127]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7713744640350342})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8674221634864807})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7819488644599915})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7768687605857849})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8835, 'crossentropy': 0.73555576171875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8314274549484253})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7677547931671143})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7517101764678955})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 32622], ['id', 19276], ['id', 36655], ['id', 42148], ['ood', 27352], ['id', 55176], ['id', 51154], ['id', 55513], ['id', 49995], ['id', 41463]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.2206583023071289, 0.3472156524658203, 0.22918939590454102, 0.3212490677833557, 0.2151573896408081, 0.45723503828048706, 0.3620717525482178, 0.4220823049545288, 0.43751198053359985, 0.38233423233032227]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8439453840255737})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7303504943847656})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.789040207862854})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7662869691848755})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7651962041854858})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.9038, 'crossentropy': 0.602761083984375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6872000694274902})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.586821436882019})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6118535995483398})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5598204135894775})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 57497], ['id', 57882], ['id', 37584], ['id', 44099], ['id', 48206], ['id', 42891], ['id', 39918], ['id', 27447], ['id', 19590], ['id', 35523]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3080582618713379, 0.5923176407814026, 0.5424845218658447, 0.4837520122528076, 0.48246169090270996, 0.5115324258804321, 0.5460622906684875, 0.5051450133323669, 0.40519773960113525, 0.33101242780685425]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8808629512786865})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6568836569786072})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7224419116973877})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7431496381759644})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.68663489818573})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.9206, 'crossentropy': 0.5491560546875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7178034782409668})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5698240399360657})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5363786220550537})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5301014184951782})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 10210], ['id', 29591], ['id', 42533], ['id', 57474], ['id', 11283], ['id', 55612], ['id', 1059], ['id', 12196], ['id', 53574], ['id', 47093]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6596269011497498, 0.4505217671394348, 0.45503079891204834, 0.577290415763855, 0.42403924465179443, 0.5691033601760864, 0.34258460998535156, 0.5153999924659729, 0.5277801752090454, 0.4359245300292969]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.893923282623291})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6374617218971252})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6350075006484985})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6625413298606873})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7149038314819336})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6878026127815247})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9124, 'crossentropy': 0.552058056640625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.735981822013855})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5904783606529236})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5358707904815674})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.499909907579422})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4976609945297241})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 55503], ['id', 8541], ['id', 55548], ['id', 51314], ['id', 49009], ['id', 26434], ['id', 40704], ['id', 45875], ['id', 47930], ['id', 18457]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6006068587303162, 0.3432603180408478, 0.4879964590072632, 0.4482020139694214, 0.5954369306564331, 0.5291702747344971, 0.40946894884109497, 0.3316802382469177, 0.37992048263549805, 0.31737813353538513]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8978036642074585})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7051664590835571})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.641323447227478})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6145503520965576})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6521313190460205})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7056684494018555})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6742665767669678})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9216, 'crossentropy': 0.53728837890625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7506018877029419})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5090619325637817})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.491736501455307})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.488960862159729})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4452836513519287})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4688988924026489})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 31628], ['id', 5103], ['id', 20989], ['id', 30474], ['id', 25586], ['id', 9428], ['ood', 52562], ['id', 5740], ['id', 39022], ['id', 8384]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4299311637878418, 0.4680800437927246, 0.589984655380249, 0.39904338121414185, 0.5806281566619873, 0.6503816246986389, 0.4360796809196472, 0.46733635663986206, 0.49516481161117554, 0.28850698471069336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8981500864028931})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6481215953826904})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6204492449760437})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6278359889984131})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6586368680000305})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6652037501335144})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9214, 'crossentropy': 0.523278662109375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7581799030303955})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5598117113113403})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5458822250366211})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5150328874588013})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.47402137517929077})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 25457], ['id', 19814], ['ood', 58568], ['id', 9180], ['id', 35480], ['id', 22438], ['id', 55162], ['id', 51544], ['id', 34698], ['id', 59362]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4192063808441162, 0.573314368724823, 0.3663538694381714, 0.5254178047180176, 0.38757026195526123, 0.3253846764564514, 0.37897789478302, 0.4797988533973694, 0.32202255725860596, 0.49747568368911743]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9754790663719177})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6869080662727356})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6413673162460327})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.67488694190979})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.594861626625061})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6518861651420593})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6279000639915466})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6872509717941284})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9206, 'crossentropy': 0.555214208984375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6703235507011414})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.554516077041626})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4968341588973999})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4929501712322235})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.45982563495635986})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4483105540275574})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.45806849002838135})
store['active_learning_steps'][12]['eval_training']['best_epoch']=6
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 11887], ['id', 53807], ['id', 42793], ['id', 18288], ['ood', 53697], ['id', 15901], ['id', 43963], ['id', 43129], ['id', 50463], ['id', 7079]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4541475772857666, 0.39211297035217285, 0.7251990437507629, 0.4651726484298706, 0.24950158596038818, 0.5877665281295776, 0.6119959354400635, 0.5174114108085632, 0.4152231216430664, 0.5022995471954346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8540530204772949})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6286110877990723})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5590763688087463})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5467888116836548})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.501635730266571})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5156220197677612})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5067054033279419})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.521015465259552})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.4638154296875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7889981269836426})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5481008291244507})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4714488983154297})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4609565734863281})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4589681625366211})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.405494749546051})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3800530433654785})
store['active_learning_steps'][13]['eval_training']['best_epoch']=7
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 16756], ['id', 34940], ['id', 37354], ['id', 11103], ['id', 7255], ['id', 1674], ['id', 19642], ['id', 45258], ['id', 26616], ['id', 25092]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5719691514968872, 0.47072458267211914, 0.29028475284576416, 0.3846518397331238, 0.406694233417511, 0.5047811269760132, 0.5497630834579468, 0.43137693405151367, 0.48522448539733887, 0.496254563331604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9167969226837158})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5296633243560791})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5327784419059753})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.527423620223999})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5291993618011475})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5602155923843384})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5572496056556702})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9308, 'crossentropy': 0.461094287109375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6592854261398315})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5181730389595032})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4441148638725281})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4312449097633362})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3989013433456421})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.40440845489501953})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 28708], ['id', 38050], ['id', 3026], ['id', 15354], ['id', 2302], ['id', 46051], ['id', 46432], ['id', 58359], ['id', 18102], ['id', 59309]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4684830904006958, 0.5912586450576782, 0.35481542348861694, 0.32346612215042114, 0.3954901695251465, 0.5624389052391052, 0.47216713428497314, 0.4575137794017792, 0.4222111701965332, 0.5161347985267639]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9933483600616455})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.565777063369751})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4949788451194763})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.47311243414878845})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5055865049362183})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5161993503570557})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5272456407546997})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9384, 'crossentropy': 0.427725146484375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6858158111572266})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.47855979204177856})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39761319756507874})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3924829959869385})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.38488149642944336})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3502495586872101})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 45516], ['id', 37978], ['id', 24965], ['id', 22931], ['id', 45998], ['id', 31672], ['id', 11997], ['id', 41540], ['id', 58560], ['id', 24124]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.42709559202194214, 0.25398752093315125, 0.3294346332550049, 0.2779219448566437, 0.3652474582195282, 0.6112219095230103, 0.511633038520813, 0.448963463306427, 0.6431148648262024, 0.3511844575405121]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.037950873374939})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5923427939414978})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5283191800117493})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5066935420036316})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5349954962730408})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5096583366394043})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48426687717437744})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5078911781311035})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5025380849838257})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5365545749664307})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9424, 'crossentropy': 0.4328400390625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8175463676452637})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5442091226577759})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4554256796836853})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4164554476737976})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3633318841457367})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.36049067974090576})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3755963146686554})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3380758464336395})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.33009082078933716})
store['active_learning_steps'][16]['eval_training']['best_epoch']=9
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 33404], ['id', 17129], ['id', 59919], ['id', 41018], ['id', 3668], ['id', 46015], ['id', 20110], ['id', 12397], ['ood', 5979], ['id', 5704]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3481922447681427, 0.5403432250022888, 0.7592208385467529, 0.5666707158088684, 0.4564344882965088, 0.638444185256958, 0.4888647794723511, 0.5420331358909607, 0.23010635375976562, 0.6284671425819397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9634432792663574})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6020189523696899})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4913720488548279})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.480099618434906})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5221003293991089})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4910276532173157})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48760730028152466})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9389, 'crossentropy': 0.432636181640625}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8290660381317139})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5201099514961243})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.43460723757743835})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4033181667327881})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.36363741755485535})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3698778748512268})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 21164], ['id', 35196], ['id', 38246], ['id', 40012], ['id', 32523], ['id', 14691], ['id', 26544], ['id', 30764], ['id', 24164], ['id', 45801]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6201933026313782, 0.3740260601043701, 0.4599952697753906, 0.4918936491012573, 0.4608188271522522, 0.44756895303726196, 0.40555524826049805, 0.4244747757911682, 0.24030399322509766, 0.4462904930114746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9579733610153198})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5360907316207886})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5427241325378418})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.433534175157547})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4231494069099426})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4687068462371826})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4731302559375763})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.38966578245162964})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41042035818099976})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.460534930229187})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48282039165496826})
store['active_learning_steps'][18]['training']['best_epoch']=8
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9498, 'crossentropy': 0.3598509521484375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7435728907585144})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4705505967140198})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.39059674739837646})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.36476337909698486})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3553430736064911})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.34219324588775635})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3386942148208618})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3103594481945038})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3231218457221985})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3096153736114502})
store['active_learning_steps'][18]['eval_training']['best_epoch']=10
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 33694], ['id', 19252], ['id', 24284], ['id', 35088], ['id', 3692], ['id', 22217], ['id', 41578], ['id', 6546], ['id', 46325], ['id', 41295]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4532080888748169, 0.2732771635055542, 0.3696657419204712, 0.3993207812309265, 0.4567856788635254, 0.41730475425720215, 0.4499850273132324, 0.34715622663497925, 0.6400728225708008, 0.4811651110649109]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8855774402618408})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5886590480804443})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.40964293479919434})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4237680435180664})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49615731835365295})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44143563508987427})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.937, 'crossentropy': 0.4066251953125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.729168176651001})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4761628806591034})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4349944591522217})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3999539911746979})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.38209593296051025})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 55791], ['id', 19505], ['ood', 34803], ['id', 54949], ['id', 21956], ['ood', 17757], ['id', 47936], ['id', 44830], ['id', 24238], ['id', 5188]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.38434898853302, 0.508288562297821, 0.28516674041748047, 0.367517352104187, 0.4513933062553406, 0.3504931926727295, 0.32823753356933594, 0.5503836870193481, 0.41808366775512695, 0.4369738698005676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8352870941162109})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4730803966522217})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.43086767196655273})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40704670548439026})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3937079608440399})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4270342290401459})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37565845251083374})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3898700773715973})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3985307216644287})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.468799352645874})
store['active_learning_steps'][20]['training']['best_epoch']=7
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9527, 'crossentropy': 0.361321533203125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7472727298736572})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4749634265899658})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.36676180362701416})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3557465076446533})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.31676292419433594})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3243114650249481})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.303228497505188})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3146149516105652})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2709081768989563})
store['active_learning_steps'][20]['eval_training']['best_epoch']=9
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 3106], ['id', 7860], ['id', 57663], ['id', 16488], ['id', 31606], ['id', 52688], ['id', 54036], ['id', 16820], ['id', 50054], ['id', 39602]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4353656768798828, 0.24298250675201416, 0.34271615743637085, 0.4199000597000122, 0.3956458270549774, 0.4137337803840637, 0.3673686385154724, 0.5087468028068542, 0.5421180129051208, 0.3680509328842163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9219004511833191})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5168927907943726})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.485562264919281})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.46327638626098633})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.417195588350296})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44049668312072754})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.42616355419158936})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47143203020095825})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9369, 'crossentropy': 0.405761328125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8275370597839355})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46587276458740234})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4028264880180359})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3639082610607147})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33811554312705994})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.34622085094451904})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.35138776898384094})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 59857], ['id', 12066], ['id', 160], ['id', 13831], ['id', 48916], ['id', 47926], ['ood', 25158], ['id', 47763], ['id', 34520], ['id', 45026]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.34965085983276367, 0.4266631007194519, 0.3345372676849365, 0.5514532923698425, 0.33668237924575806, 0.37941890954971313, 0.19502043724060059, 0.2849496603012085, 0.4230691194534302, 0.4753982424736023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.016188383102417})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5206796526908875})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4204099178314209})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3935283124446869})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38094770908355713})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3596178889274597})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38164541125297546})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.47194427251815796})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4003834128379822})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9558, 'crossentropy': 0.3398236083984375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6744478940963745})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44009920954704285})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35339289903640747})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3396173417568207})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30978459119796753})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3266754746437073})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.267267644405365})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28761690855026245})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 13247], ['id', 39389], ['id', 10555], ['id', 49728], ['ood', 54041], ['id', 14722], ['id', 33505], ['id', 56454], ['id', 30517], ['id', 46274]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.35959696769714355, 0.4147716164588928, 0.5124172568321228, 0.5210351347923279, 0.1917632818222046, 0.5494160652160645, 0.5563323497772217, 0.43143516778945923, 0.33210572600364685, 0.4545604884624481]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9769288301467896})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5374451279640198})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40800905227661133})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33177506923675537})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37641459703445435})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3835132122039795})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35553014278411865})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9565, 'crossentropy': 0.3247111083984375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8225350379943848})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.478481262922287})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4104250967502594})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4276321828365326})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.350561261177063})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3697282075881958})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 54043], ['id', 53872], ['id', 23079], ['ood', 49253], ['id', 1160], ['id', 45187], ['id', 540], ['id', 9390], ['id', 13524], ['id', 31512]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5039026737213135, 0.3556509017944336, 0.3247023820877075, 0.2279965877532959, 0.3698611259460449, 0.33410459756851196, 0.21517473459243774, 0.47268009185791016, 0.5285465717315674, 0.486449658870697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.115788459777832})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5659039616584778})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.43492674827575684})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38364291191101074})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4275297522544861})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43843352794647217})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3877299129962921})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9449, 'crossentropy': 0.379242578125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.814455509185791})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5001431703567505})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.46277642250061035})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.41126418113708496})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4038010239601135})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3987862467765808})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 10044], ['id', 28666], ['id', 17005], ['id', 52896], ['id', 37842], ['id', 55052], ['id', 31557], ['id', 39031], ['ood', 49147], ['id', 9645]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.28099268674850464, 0.32619917392730713, 0.4480552673339844, 0.31312286853790283, 0.31661367416381836, 0.5153765678405762, 0.4672967195510864, 0.4481234550476074, 0.1700897216796875, 0.32707875967025757]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.035210371017456})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5101341009140015})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42291226983070374})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36707621812820435})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30618786811828613})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3348226845264435})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33579879999160767})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3683585226535797})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9615, 'crossentropy': 0.302873388671875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8017492294311523})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5350229740142822})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3931526243686676})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33579766750335693})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3167029321193695})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3208685517311096})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2894290089607239})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 46022], ['id', 27125], ['id', 14105], ['id', 18904], ['id', 8366], ['id', 38252], ['id', 23459], ['id', 1840], ['id', 19138], ['id', 9340]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3207065463066101, 0.4290115237236023, 0.4847261905670166, 0.4252064526081085, 0.337935209274292, 0.37172645330429077, 0.3291124701499939, 0.4537057876586914, 0.4225119352340698, 0.43571561574935913]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9698891639709473})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5052434206008911})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3727416396141052})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3600096106529236})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3437821865081787})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33202239871025085})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3128417432308197})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35395684838294983})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34461987018585205})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35224735736846924})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9638, 'crossentropy': 0.2970896240234375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8762609958648682})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49118685722351074})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3547494411468506})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33012378215789795})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32446154952049255})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31669533252716064})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30065250396728516})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29815250635147095})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27624621987342834})
store['active_learning_steps'][26]['eval_training']['best_epoch']=9
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 15068], ['id', 51759], ['id', 18601], ['id', 52392], ['id', 44261], ['id', 32668], ['id', 9791], ['id', 28189], ['id', 29182], ['id', 22270]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5877277851104736, 0.47535401582717896, 0.2887172996997833, 0.7657400965690613, 0.37886661291122437, 0.6404263973236084, 0.33263498544692993, 0.44245362281799316, 0.49225133657455444, 0.3401098847389221]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0376999378204346})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.533945620059967})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36550241708755493})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3629310727119446})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3457241952419281})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33741873502731323})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28744304180145264})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2881007790565491})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3035927414894104})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.3036397099494934})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9657, 'crossentropy': 0.281713427734375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8386745452880859})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47018030285835266})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.40088385343551636})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33592236042022705})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3114505410194397})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28830426931381226})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28935304284095764})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30066752433776855})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28600338101387024})
store['active_learning_steps'][27]['eval_training']['best_epoch']=9
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 1259], ['id', 32421], ['id', 39208], ['id', 34188], ['id', 2765], ['id', 12840], ['id', 17131], ['id', 39573], ['id', 20792], ['id', 45019]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.31739211082458496, 0.44266098737716675, 0.6097126603126526, 0.5770924687385559, 0.5567877292633057, 0.5127725005149841, 0.45581895112991333, 0.48957836627960205, 0.43011975288391113, 0.48442113399505615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.977710485458374})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5170915722846985})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4016469120979309})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3480331301689148})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3550304174423218})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32593396306037903})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3166278600692749})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30899685621261597})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3211311995983124})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3090125620365143})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3570387363433838})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9634, 'crossentropy': 0.2836410400390625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7823327779769897})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46731215715408325})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37521934509277344})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3298577070236206})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2916470766067505})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2563145160675049})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2679486870765686})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2529682517051697})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25858351588249207})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2572265863418579})
store['active_learning_steps'][28]['eval_training']['best_epoch']=8
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 12889], ['id', 14904], ['ood', 58398], ['id', 55294], ['ood', 26892], ['id', 57205], ['id', 9567], ['id', 10195], ['id', 2381], ['id', 1116]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3010719418525696, 0.3733142614364624, 0.3548811674118042, 0.48708778619766235, 0.34664130210876465, 0.37770724296569824, 0.37420976161956787, 0.45374244451522827, 0.4842718243598938, 0.4151793420314789]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 1.006485939025879})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5788223147392273})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3882421851158142})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32395118474960327})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3171352744102478})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29650983214378357})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30299586057662964})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27080613374710083})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.310646116733551})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3029881715774536})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.291251540184021})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.2509477783203125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8481964468955994})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47993817925453186})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.32892972230911255})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3130757212638855})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26091039180755615})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26866811513900757})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2729056775569916})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2493213415145874})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25310730934143066})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26782530546188354})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 28413], ['id', 32747], ['id', 30838], ['ood', 48824], ['id', 28506], ['id', 30968], ['id', 41933], ['id', 35864], ['id', 49908], ['id', 55073]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4553067088127136, 0.6558801531791687, 0.4413396716117859, 0.34213364124298096, 0.6100344657897949, 0.45440399646759033, 0.49169957637786865, 0.6324706077575684, 0.4908331036567688, 0.3499588966369629]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0761964321136475})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5432077646255493})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3649146556854248})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35385358333587646})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3017767071723938})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2794858515262604})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3303784728050232})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2783966064453125})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2889021635055542})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29742157459259033})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3220268785953522})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9662, 'crossentropy': 0.26755732421875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7416220903396606})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4680548310279846})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36410632729530334})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.297627717256546})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29503101110458374})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26890724897384644})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28797411918640137})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2647055685520172})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2534472346305847})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25252872705459595})
store['active_learning_steps'][30]['eval_training']['best_epoch']=10
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 1035], ['id', 48997], ['id', 6466], ['id', 34524], ['id', 24479], ['id', 20718], ['id', 32397], ['ood', 24325], ['id', 38626], ['id', 45016]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.40147221088409424, 0.3081250488758087, 0.6038049459457397, 0.5374805927276611, 0.42677921056747437, 0.4090312123298645, 0.472045361995697, 0.3348579406738281, 0.46455276012420654, 0.3979312777519226]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.135783314704895})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5030995607376099})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3897474408149719})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32579323649406433})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3040872812271118})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2897895574569702})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3094879388809204})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26703059673309326})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2661812901496887})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25665563344955444})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.26030051708221436})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.301170289516449})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2865141034126282})
store['active_learning_steps'][31]['training']['best_epoch']=10
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.25229609375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8260782957077026})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.48800933361053467})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3391948938369751})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3345112204551697})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3028595447540283})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27485576272010803})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27076858282089233})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2623874545097351})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25515061616897583})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24365970492362976})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27484965324401855})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2456003725528717})
store['active_learning_steps'][31]['eval_training']['best_epoch']=10
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 20663], ['ood', 20232], ['id', 30085], ['id', 14128], ['id', 22505], ['id', 27348], ['id', 40259], ['id', 16797], ['id', 30228], ['ood', 54159]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.44863831996917725, 0.35690033435821533, 0.5327054858207703, 0.35770368576049805, 0.5032789707183838, 0.5397301316261292, 0.49853718280792236, 0.5061402320861816, 0.4966033101081848, 0.4329739809036255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.2516942024230957})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6077708005905151})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4303724765777588})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35821297764778137})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.320659339427948})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32198476791381836})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3123821020126343})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.289619505405426})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3219608664512634})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2915620803833008})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31817322969436646})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.276305126953125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8959091305732727})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4951443076133728})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38193976879119873})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38027262687683105})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30372071266174316})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.26221364736557007})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29267576336860657})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.3093251585960388})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28605806827545166})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 51432], ['id', 3810], ['id', 37680], ['id', 27265], ['id', 20867], ['id', 50740], ['id', 51738], ['id', 59283], ['id', 55264], ['id', 40066]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.45301395654678345, 0.5814786553382874, 0.48116907477378845, 0.29268765449523926, 0.5013035535812378, 0.3663182258605957, 0.49395373463630676, 0.5075478553771973, 0.5141095519065857, 0.2520493268966675]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0267770290374756})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6570539474487305})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.45238280296325684})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3340887129306793})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33653274178504944})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30356544256210327})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29379987716674805})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2995564341545105})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2976604104042053})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28470128774642944})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33516305685043335})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31570643186569214})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32637301087379456})
store['active_learning_steps'][33]['training']['best_epoch']=10
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.2814049560546875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8885174989700317})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4631110429763794})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.367777943611145})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3256276845932007})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33545351028442383})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2917518615722656})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2621828317642212})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26093360781669617})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.273330420255661})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26919829845428467})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25598669052124023})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26471951603889465})
store['active_learning_steps'][33]['eval_training']['best_epoch']=11
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 132], ['id', 36072], ['id', 59701], ['id', 31301], ['id', 48584], ['id', 13099], ['id', 7793], ['id', 47599], ['id', 37529], ['id', 4103]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5202161073684692, 0.6121906638145447, 0.5180651545524597, 0.6204728484153748, 0.4918760061264038, 0.47383320331573486, 0.6053029298782349, 0.49262183904647827, 0.5869460701942444, 0.1719793677330017]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0858924388885498})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5549504160881042})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4893777370452881})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3881380558013916})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35063856840133667})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.296189546585083})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2987419068813324})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32820332050323486})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.298115074634552})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.964, 'crossentropy': 0.2811892822265625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8970153331756592})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5385748147964478})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.389926552772522})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33434805274009705})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2972604036331177})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3061748743057251})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29460111260414124})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2709819972515106})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 18487], ['id', 3289], ['ood', 30489], ['id', 30359], ['id', 9770], ['id', 48065], ['id', 53482], ['id', 14062], ['id', 18654], ['id', 57546]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.3791165351867676, 0.38388025760650635, 0.3141592741012573, 0.40319961309432983, 0.40631091594696045, 0.38671624660491943, 0.4252294898033142, 0.4772682189941406, 0.47063493728637695, 0.2207367718219757]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.263301134109497})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5808044672012329})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42058366537094116})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.353861927986145})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3445177674293518})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2932145595550537})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2954283654689789})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2746009826660156})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.32162636518478394})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2851543426513672})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2965647876262665})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.25880732421875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.848301112651825})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.47455745935440063})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37267130613327026})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3292301297187805})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3197825849056244})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2843053936958313})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2512112855911255})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30615001916885376})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26307088136672974})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.261436402797699})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 704], ['id', 17406], ['id', 14290], ['id', 43548], ['id', 19188], ['id', 47549], ['id', 55958], ['id', 47274], ['ood', 42326], ['id', 50896]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3522023558616638, 0.4050835371017456, 0.33311688899993896, 0.3424443006515503, 0.3773818910121918, 0.43303632736206055, 0.2630503475666046, 0.39068758487701416, 0.3068196773529053, 0.2804921865463257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1794638633728027})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5572776794433594})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33889371156692505})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31636595726013184})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2951540946960449})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29917824268341064})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28924983739852905})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26894327998161316})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2886197566986084})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2963680624961853})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29358720779418945})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.2553002685546875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8116888999938965})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.44964951276779175})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.40644994378089905})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33958661556243896})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30788737535476685})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3021044135093689})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3078916668891907})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2604443430900574})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2724040746688843})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2716037631034851})
store['active_learning_steps'][36]['eval_training']['best_epoch']=8
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 55906], ['id', 14796], ['id', 52869], ['id', 53309], ['id', 31197], ['id', 26405], ['id', 6347], ['id', 6905], ['id', 43943], ['id', 36450]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5161481499671936, 0.5484541654586792, 0.633863091468811, 0.27572542428970337, 0.44693541526794434, 0.5326389074325562, 0.457804799079895, 0.45950448513031006, 0.2651212811470032, 0.47592175006866455]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.18223237991333})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5908629894256592})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4287671446800232})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32391810417175293})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3242601156234741})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2981072664260864})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29069793224334717})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2697773277759552})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28046339750289917})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.290757954120636})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2694801092147827})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.331257700920105})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2845001220703125})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29445457458496094})
store['active_learning_steps'][37]['training']['best_epoch']=11
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9742, 'crossentropy': 0.24633837890625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0152182579040527})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5962547659873962})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4429164528846741})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3653753399848938})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3104448914527893})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2842046618461609})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2739901840686798})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23784147202968597})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2659090757369995})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2592797577381134})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2351948469877243})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25533348321914673})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2608928680419922})
store['active_learning_steps'][37]['eval_training']['best_epoch']=11
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 56014], ['id', 45091], ['id', 27336], ['id', 9320], ['id', 46023], ['ood', 37468], ['id', 52151], ['id', 20636], ['id', 13242], ['id', 54992]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.46752482652664185, 0.44321322441101074, 0.31011128425598145, 0.3489301800727844, 0.46190428733825684, 0.45804595947265625, 0.35588371753692627, 0.42019182443618774, 0.49165886640548706, 0.3362380862236023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1810462474822998})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5474305152893066})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3929774761199951})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3197000026702881})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2847062945365906})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2722887694835663})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2642553150653839})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2896779775619507})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29914000630378723})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26143312454223633})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2813867926597595})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2958278954029083})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2824384570121765})
store['active_learning_steps'][38]['training']['best_epoch']=10
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9692, 'crossentropy': 0.2643780029296875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8546059131622314})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4723477363586426})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3673193156719208})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3331531882286072})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32243698835372925})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30018359422683716})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2614639401435852})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2616199254989624})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24396154284477234})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.23653647303581238})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.26009291410446167})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23959803581237793})
store['active_learning_steps'][38]['eval_training']['best_epoch']=10
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 9651], ['id', 45056], ['id', 47473], ['id', 854], ['id', 34538], ['id', 35486], ['id', 391], ['id', 40236], ['id', 30960], ['id', 11074]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5036761164665222, 0.4409298300743103, 0.48468637466430664, 0.42088156938552856, 0.3115308880805969, 0.2658560574054718, 0.5714513063430786, 0.51148521900177, 0.3750059902667999, 0.3824925422668457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0485233068466187})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4827321171760559})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3564354181289673})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2961353063583374})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29431581497192383})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2875428795814514})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30130326747894287})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2795717716217041})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2675027847290039})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.303081214427948})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2564387321472168})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25574791431427})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3033715486526489})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2836296856403351})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2908216118812561})
store['active_learning_steps'][39]['training']['best_epoch']=12
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9734, 'crossentropy': 0.22571708984375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9008902311325073})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5211719870567322})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3572733402252197})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34662437438964844})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31472262740135193})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30188435316085815})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2817581295967102})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2834908068180084})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23123590648174286})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25968676805496216})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2597407102584839})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2385667860507965})
store['active_learning_steps'][39]['eval_training']['best_epoch']=9
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 45666], ['id', 38142], ['id', 48382], ['id', 28374], ['ood', 42336], ['id', 22632], ['id', 8689], ['id', 24940], ['id', 31591], ['id', 14749]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5911444425582886, 0.3955085873603821, 0.5117494463920593, 0.39216339588165283, 0.42821764945983887, 0.4631614685058594, 0.48513683676719666, 0.38801297545433044, 0.49185675382614136, 0.5996244549751282]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.1585900783538818})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5835869312286377})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4239078760147095})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38164281845092773})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31595277786254883})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31296443939208984})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26480984687805176})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30468112230300903})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32565149664878845})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30551013350486755})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.2606173828125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0237672328948975})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6057233810424805})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4372745156288147})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.41441598534584045})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.33912113308906555})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34593531489372253})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32410675287246704})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3381028473377228})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31472456455230713})
store['active_learning_steps'][40]['eval_training']['best_epoch']=9
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 23678], ['id', 32276], ['id', 256], ['id', 26302], ['id', 10925], ['id', 6980], ['id', 46780], ['id', 43126], ['id', 47292], ['id', 42355]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.47607794404029846, 0.4501652121543884, 0.319274365901947, 0.41756194829940796, 0.438634991645813, 0.5544260144233704, 0.44560539722442627, 0.5989679098129272, 0.43009698390960693, 0.35646265745162964]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1438997983932495})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5393256545066833})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37574827671051025})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3209160566329956})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27073055505752563})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2586599290370941})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24928918480873108})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24282106757164001})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2738644480705261})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.300159215927124})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2675817608833313})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.2297833251953125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8388196229934692})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.531041145324707})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.42109107971191406})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29664358496665955})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31895169615745544})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2899269163608551})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.256390780210495})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2538461685180664})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23668354749679565})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28196054697036743})
store['active_learning_steps'][41]['eval_training']['best_epoch']=9
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 26705], ['id', 47690], ['id', 30357], ['id', 52886], ['id', 14385], ['id', 59314], ['id', 25190], ['id', 28199], ['id', 42715], ['id', 28930]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.39083391427993774, 0.4209766387939453, 0.4734620153903961, 0.33062803745269775, 0.385437548160553, 0.5468493700027466, 0.23044727742671967, 0.39121174812316895, 0.49746549129486084, 0.5263480544090271]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.1498723030090332})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.5459718704223633})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4256879687309265})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3574303984642029})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2859652638435364})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25645631551742554})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28820058703422546})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.23710715770721436})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24673254787921906})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26818275451660156})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24554425477981567})
store['active_learning_steps'][42]['training']['best_epoch']=8
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9693, 'crossentropy': 0.2537355224609375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.9812356233596802})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.530667781829834})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40054887533187866})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35664620995521545})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32994431257247925})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27381089329719543})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3024406433105469})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29419147968292236})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2605004906654358})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2546986937522888})
store['active_learning_steps'][42]['eval_training']['best_epoch']=10
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 5129], ['id', 21128], ['id', 11964], ['id', 7612], ['id', 43950], ['id', 1512], ['id', 46435], ['id', 54954], ['id', 55396], ['id', 1135]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5083613395690918, 0.32546770572662354, 0.3708096742630005, 0.5367342829704285, 0.5134567022323608, 0.46152758598327637, 0.341653972864151, 0.3039131164550781, 0.502994179725647, 0.4800872206687927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1968843936920166})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6174756288528442})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.40644747018814087})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29981881380081177})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29452359676361084})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2440357506275177})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2594067454338074})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24706971645355225})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25689494609832764})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.2310085693359375}
