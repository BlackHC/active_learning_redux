store = {}
store['timestamp']=1621039172
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=24']
store['commit']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['github_url']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=24
store['worker_id']=24
store['num_workers']=30
store['config']={'seed': 1266, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.EvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset: FastMNIST (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.6730666160583496})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.8378591537475586})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.3676321506500244})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.5308666229248047})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5789, 'crossentropy': 2.58879453125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.3263731002807617})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.328049898147583})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.328003168106079})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 25994], ['ood', 37941], ['ood', 26106], ['ood', 33565], ['ood', 36400], ['ood', 32065], ['ood', 39386], ['ood', 4336], ['ood', 39970], ['ood', 46487]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9143546223640442, 0.887645423412323, 0.8807893395423889, 0.8765493631362915, 0.8746814727783203, 0.869953989982605, 0.8649327158927917, 0.8626540303230286, 0.8626090884208679, 0.8608968257904053]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 2.3261966705322266})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.942702054977417})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.2050023078918457})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.7373523712158203})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5558, 'crossentropy': 2.2898705078125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.338600516319275})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.4017490148544312})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.269441843032837})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 19658], ['id', 45640], ['id', 9409], ['id', 18729], ['id', 50542], ['id', 54101], ['id', 41273], ['id', 12019], ['ood', 56081], ['id', 36215]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5935662388801575, 0.5865606069564819, 0.5811356902122498, 0.5792460441589355, 0.5685415267944336, 0.5648592710494995, 0.5629768371582031, 0.5609764456748962, 0.5603905916213989, 0.5575984120368958]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.798978328704834})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.391953468322754})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.8501906394958496})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.246115207672119})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5673, 'crossentropy': 1.771954296875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.3710417747497559})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 1.3287160396575928})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.2986035346984863})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 45967], ['id', 472], ['id', 21828], ['id', 39789], ['id', 25868], ['id', 49349], ['id', 46576], ['id', 45708], ['id', 25747], ['id', 4306]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5367644429206848, 0.5291548371315002, 0.5236899256706238, 0.5227513909339905, 0.5221800804138184, 0.5221661925315857, 0.5215603113174438, 0.5192818641662598, 0.5118284821510315, 0.5112443566322327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.544921875, 'crossentropy': 1.502909779548645})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.225078821182251})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 2.577385425567627})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 2.728144884109497})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5516, 'crossentropy': 1.510974609375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.3790783882141113})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.54296875, 'crossentropy': 1.3353571891784668})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.3148951530456543})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 22634], ['ood', 46597], ['ood', 44955], ['ood', 6917], ['ood', 52650], ['ood', 9699], ['ood', 56866], ['ood', 28471], ['ood', 37740], ['ood', 49784]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4247913360595703, 0.4097381830215454, 0.40767180919647217, 0.40724706649780273, 0.40452325344085693, 0.4031565189361572, 0.3991185426712036, 0.39871156215667725, 0.39602208137512207, 0.3946959972381592]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5390625, 'crossentropy': 1.6246099472045898})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.8312715291976929})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.046635866165161})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.364323616027832})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5392, 'crossentropy': 1.58707919921875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.494140625, 'crossentropy': 1.4905719757080078})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5107421875, 'crossentropy': 1.5015652179718018})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5087890625, 'crossentropy': 1.4687256813049316})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 8879], ['id', 1799], ['id', 53134], ['id', 20345], ['id', 8485], ['id', 58110], ['id', 59682], ['ood', 5790], ['id', 35699], ['id', 4619]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3339040279388428, 0.33101797103881836, 0.3257730007171631, 0.3238643407821655, 0.3223453760147095, 0.3216872215270996, 0.3216770887374878, 0.3211941719055176, 0.3176417350769043, 0.3162592649459839]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.55078125, 'crossentropy': 1.5175485610961914})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.6702711582183838})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.936671257019043})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.4576053619384766})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5414, 'crossentropy': 1.5300966796875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.4951171875, 'crossentropy': 1.4367952346801758})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.517578125, 'crossentropy': 1.4426820278167725})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.525390625, 'crossentropy': 1.4046162366867065})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 45484], ['ood', 50479], ['ood', 51506], ['ood', 56964], ['ood', 40394], ['ood', 59152], ['ood', 49409], ['ood', 10736], ['ood', 23080], ['ood', 50441]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.37054872512817383, 0.3691716194152832, 0.36910271644592285, 0.3685765266418457, 0.368499755859375, 0.36662018299102783, 0.3636070489883423, 0.3495469093322754, 0.3495030403137207, 0.3491816520690918]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.4285621643066406})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.3651745319366455})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.7324695587158203})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.9016814231872559})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.1082170009613037})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6314, 'crossentropy': 1.353845703125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.1983197927474976})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.1367732286453247})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1025303602218628})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1214122772216797})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 14791], ['id', 54542], ['id', 59771], ['id', 6841], ['id', 59703], ['id', 21810], ['id', 52509], ['id', 24282], ['id', 12467], ['id', 55368]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4514896869659424, 0.443729043006897, 0.4328954219818115, 0.41204798221588135, 0.4055519104003906, 0.401513934135437, 0.39944708347320557, 0.39698922634124756, 0.39690136909484863, 0.39347660541534424]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.525390625, 'crossentropy': 1.4589784145355225})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.3423347473144531})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.451415777206421})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.797404170036316})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.7937424182891846})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6178, 'crossentropy': 1.35935615234375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.2225863933563232})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.1941527128219604})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.136275053024292})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.1590747833251953})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 1180], ['id', 58242], ['id', 33166], ['id', 50431], ['id', 18444], ['id', 31897], ['id', 24018], ['id', 27581], ['id', 3732], ['id', 57959]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4535442590713501, 0.4485738277435303, 0.44001245498657227, 0.4381147623062134, 0.42650890350341797, 0.4252948760986328, 0.4249229431152344, 0.42447423934936523, 0.41875386238098145, 0.41542696952819824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.396279215812683})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.3285636901855469})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4254695177078247})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.5913777351379395})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.9514658451080322})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6148, 'crossentropy': 1.35957900390625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.2708642482757568})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.1693854331970215})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.1840012073516846})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.1500290632247925})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 44871], ['id', 20398], ['id', 37438], ['id', 7076], ['id', 25195], ['id', 49759], ['id', 25672], ['id', 24901], ['id', 33387], ['id', 326]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.44214534759521484, 0.43807363510131836, 0.4129762649536133, 0.4007188081741333, 0.3983703851699829, 0.39237844944000244, 0.3917839527130127, 0.38942623138427734, 0.38941991329193115, 0.38879507780075073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.541015625, 'crossentropy': 1.4317142963409424})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.2899893522262573})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.394063949584961})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.9056882858276367})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.9878389835357666})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5962, 'crossentropy': 1.31779443359375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.2552356719970703})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.2165895700454712})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.1823378801345825})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.1846652030944824})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 56627], ['id', 38058], ['id', 7746], ['id', 43234], ['id', 18952], ['id', 35292], ['id', 25465], ['id', 6348], ['id', 49790], ['id', 28844]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.37803518772125244, 0.3726613521575928, 0.3715170621871948, 0.3691117763519287, 0.3676851987838745, 0.36309897899627686, 0.3621811866760254, 0.36113739013671875, 0.36020851135253906, 0.3598262071609497]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.402698278427124})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2494041919708252})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.4153125286102295})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.5380220413208008})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.605652093887329})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6419, 'crossentropy': 1.241485546875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2571899890899658})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.1886885166168213})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.1657977104187012})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.1564538478851318})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 10319], ['ood', 1586], ['id', 26174], ['id', 57504], ['id', 55037], ['id', 27409], ['id', 45740], ['ood', 9880], ['ood', 12411], ['ood', 33426]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3493635654449463, 0.3157169818878174, 0.3111128807067871, 0.30827367305755615, 0.3030077815055847, 0.30133330821990967, 0.3002455234527588, 0.3001673221588135, 0.2978017330169678, 0.29756081104278564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.53125, 'crossentropy': 1.4202191829681396})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2510051727294922})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2648591995239258})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.3558400869369507})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.5926883220672607})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6484, 'crossentropy': 1.249471875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.255147933959961})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2219951152801514})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.174414873123169})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.208963394165039})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 46300], ['id', 3300], ['id', 21487], ['id', 2369], ['ood', 8731], ['id', 11862], ['id', 2731], ['id', 6844], ['ood', 16956], ['ood', 28886]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4087061882019043, 0.40109437704086304, 0.3746687173843384, 0.369484007358551, 0.36768728494644165, 0.36488842964172363, 0.36180830001831055, 0.36175233125686646, 0.3594566583633423, 0.3547220230102539]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5166015625, 'crossentropy': 1.4746451377868652})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2403874397277832})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.21392023563385})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.4059114456176758})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.5710864067077637})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.5744209289550781})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6483, 'crossentropy': 1.27920498046875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2220313549041748})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.0994174480438232})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.056578516960144})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.0859827995300293})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.0732285976409912})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 8986], ['id', 24953], ['id', 7375], ['id', 32498], ['id', 15124], ['id', 4713], ['id', 50403], ['id', 48595], ['id', 57174], ['id', 11724]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.42200541496276855, 0.4054484963417053, 0.3989049792289734, 0.382540225982666, 0.37885522842407227, 0.371895432472229, 0.3686080574989319, 0.3684117794036865, 0.3664752244949341, 0.3649466633796692]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.525390625, 'crossentropy': 1.4182953834533691})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.303307056427002})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.317274808883667})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.4275540113449097})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.5949937105178833})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6144, 'crossentropy': 1.2885876953125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.3390686511993408})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.2603914737701416})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.2131359577178955})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2138490676879883})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 16154], ['id', 41355], ['id', 54405], ['id', 34994], ['id', 35684], ['id', 21562], ['id', 70], ['id', 16309], ['id', 34336], ['id', 3944]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.31571364402770996, 0.3072037696838379, 0.28581416606903076, 0.2826054096221924, 0.2753232717514038, 0.27163374423980713, 0.26948654651641846, 0.26942873001098633, 0.26933062076568604, 0.2692621946334839]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.4087867736816406})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2015650272369385})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2416365146636963})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2798964977264404})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.429629921913147})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6323, 'crossentropy': 1.22334599609375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.3432124853134155})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.2411607503890991})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1954864263534546})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.178311824798584})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 27800], ['id', 14410], ['id', 30476], ['id', 2181], ['id', 54813], ['id', 13598], ['id', 34314], ['id', 22547], ['id', 35305], ['id', 52428]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.35791444778442383, 0.33368074893951416, 0.3269540071487427, 0.32450199127197266, 0.31876426935195923, 0.317844033241272, 0.31580257415771484, 0.3130608797073364, 0.30448079109191895, 0.3043205738067627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5244140625, 'crossentropy': 1.4518827199935913})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.231451153755188})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2309439182281494})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2767493724822998})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3777267932891846})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.4310067892074585})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.658, 'crossentropy': 1.189581640625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.2684600353240967})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1345962285995483})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1137466430664062})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.0780088901519775})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.081498384475708})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 38806], ['id', 3410], ['id', 36424], ['id', 28159], ['id', 28543], ['id', 43193], ['id', 58130], ['id', 56380], ['id', 21011], ['id', 23414]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.35182952880859375, 0.3472161293029785, 0.3268486261367798, 0.31799066066741943, 0.31741654872894287, 0.3160130977630615, 0.31509971618652344, 0.31457817554473877, 0.31368565559387207, 0.3130300045013428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.505859375, 'crossentropy': 1.47392737865448})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2241954803466797})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.257584571838379})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3512473106384277})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3555214405059814})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6183, 'crossentropy': 1.2193224609375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.3118025064468384})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.2307968139648438})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2024624347686768})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.2079120874404907})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 26636], ['id', 7456], ['id', 57297], ['id', 12701], ['id', 40029], ['id', 3343], ['id', 34920], ['id', 58560], ['id', 45778], ['id', 34833]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3600696325302124, 0.3145213723182678, 0.29664862155914307, 0.29648709297180176, 0.29437530040740967, 0.2943202257156372, 0.2926722764968872, 0.29266905784606934, 0.28673267364501953, 0.28270041942596436]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.4560546875, 'crossentropy': 1.5536727905273438})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.2903592586517334})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.2555303573608398})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2010606527328491})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.274733304977417})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.4344604015350342})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.489918828010559})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6521, 'crossentropy': 1.269023046875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.273399829864502})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1450659036636353})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1329658031463623})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0784562826156616})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0771245956420898})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.068885326385498})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 50611], ['id', 17871], ['id', 23295], ['id', 54712], ['id', 2372], ['id', 50879], ['id', 19136], ['id', 35668], ['id', 628], ['id', 12426]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.45474398136138916, 0.43561112880706787, 0.42842036485671997, 0.4215738773345947, 0.41911303997039795, 0.41616153717041016, 0.4159066081047058, 0.40941470861434937, 0.4072909951210022, 0.4035395383834839]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.4609375, 'crossentropy': 1.4953688383102417})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.2782371044158936})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2008793354034424})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2193760871887207})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2255562543869019})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.4294726848602295})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6382, 'crossentropy': 1.22495439453125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.2700119018554688})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1735070943832397})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.1351274251937866})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1170072555541992})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.1211525201797485})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 6256], ['id', 9302], ['id', 49777], ['id', 10568], ['id', 24192], ['id', 51064], ['id', 44331], ['id', 28510], ['id', 15495], ['id', 9954]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.3593308925628662, 0.35599303245544434, 0.3535740375518799, 0.35223472118377686, 0.3471869230270386, 0.3428157567977905, 0.34118008613586426, 0.33338606357574463, 0.33321213722229004, 0.3332064151763916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.470703125, 'crossentropy': 1.5172271728515625})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.2817347049713135})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1983113288879395})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.253588318824768})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2367453575134277})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.4233031272888184})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6361, 'crossentropy': 1.193253125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.2588932514190674})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.1577222347259521})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.0946035385131836})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1376031637191772})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.084017276763916})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 31662], ['id', 33674], ['id', 33141], ['id', 27260], ['id', 55968], ['id', 37251], ['id', 57751], ['id', 27184], ['id', 57944], ['id', 28546]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3965597152709961, 0.3733701705932617, 0.368585467338562, 0.36788058280944824, 0.36084771156311035, 0.35482072830200195, 0.3517635464668274, 0.35145044326782227, 0.34610313177108765, 0.34570300579071045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.4345703125, 'crossentropy': 1.5562211275100708})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.263085126876831})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.131399393081665})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1692500114440918})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.214076042175293})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.330269455909729})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6612, 'crossentropy': 1.1589189453125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.3352320194244385})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.2179808616638184})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.151826024055481})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1969510316848755})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1685984134674072})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 5692], ['id', 20638], ['id', 2576], ['id', 19855], ['id', 40800], ['id', 50381], ['id', 38347], ['id', 2464], ['id', 25184], ['id', 5042]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3804280757904053, 0.3680593967437744, 0.36544859409332275, 0.36536312103271484, 0.359655499458313, 0.35897183418273926, 0.35713493824005127, 0.3561384677886963, 0.3559761047363281, 0.35317862033843994]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.4267578125, 'crossentropy': 1.590834140777588})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.2857898473739624})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.268702507019043})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.220853328704834})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.4034817218780518})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.3949837684631348})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3695725202560425})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6483, 'crossentropy': 1.2001162109375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.298398733139038})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1542584896087646})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.117241382598877})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.0508761405944824})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.0636217594146729})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0112563371658325})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 17646], ['id', 53365], ['id', 4196], ['id', 39579], ['id', 51720], ['id', 8669], ['id', 10509], ['id', 28390], ['id', 13187], ['id', 10754]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.390987753868103, 0.3882952928543091, 0.3881118893623352, 0.38771212100982666, 0.3829936981201172, 0.3812413215637207, 0.38041818141937256, 0.3802757263183594, 0.3798409700393677, 0.37752485275268555]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5068359375, 'crossentropy': 1.513617992401123})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.2891292572021484})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.184593915939331})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1367437839508057})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.127838373184204})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1559545993804932})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1928958892822266})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.3157708644866943})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6873, 'crossentropy': 1.108292578125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2714561223983765})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1351592540740967})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0574164390563965})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0579758882522583})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0232360363006592})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.029647946357727})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0062243938446045})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 5346], ['id', 18675], ['id', 3913], ['id', 20624], ['id', 9692], ['id', 36091], ['id', 59072], ['id', 8763], ['id', 45096], ['id', 7593]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.44864070415496826, 0.39788806438446045, 0.37736523151397705, 0.3721047639846802, 0.36735105514526367, 0.3640252351760864, 0.36366283893585205, 0.3633418083190918, 0.35637903213500977, 0.350952684879303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.490234375, 'crossentropy': 1.4854867458343506})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2513389587402344})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1550251245498657})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.203852653503418})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.153630018234253})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3051886558532715})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2858784198760986})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.4434154033660889})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6874, 'crossentropy': 1.13455068359375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.330197811126709})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0735588073730469})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0431537628173828})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0409401655197144})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 0.9884278178215027})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0005178451538086})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.012774109840393})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 55098], ['id', 3830], ['id', 18487], ['id', 49055], ['id', 49338], ['id', 26818], ['id', 21535], ['id', 59953], ['id', 56682], ['id', 20867]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.42889440059661865, 0.40897631645202637, 0.39414238929748535, 0.38204866647720337, 0.3792541027069092, 0.36798715591430664, 0.36759841442108154, 0.3636298179626465, 0.3619840741157532, 0.36143791675567627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5390625, 'crossentropy': 1.5456902980804443})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.2827121019363403})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.140736699104309})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.183995246887207})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1344707012176514})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1806788444519043})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2299703359603882})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.2658683061599731})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6872, 'crossentropy': 1.12846552734375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.2440476417541504})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0694739818572998})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0336952209472656})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.007530927658081})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0021750926971436})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 0.9716291427612305})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 0.969237208366394})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 45167], ['id', 20009], ['id', 1031], ['id', 54732], ['id', 43830], ['id', 44245], ['id', 14664], ['id', 32177], ['id', 37896], ['id', 49814]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5232070088386536, 0.4626436233520508, 0.46169471740722656, 0.4418238401412964, 0.4281112551689148, 0.42527854442596436, 0.42022931575775146, 0.4183039665222168, 0.41666561365127563, 0.4084465503692627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5234375, 'crossentropy': 1.5236270427703857})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.2352906465530396})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.1724965572357178})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1306536197662354})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1269636154174805})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1415133476257324})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.2714802026748657})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.2384692430496216})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6815, 'crossentropy': 1.1465580078125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.2480614185333252})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0973467826843262})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.0716099739074707})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0768396854400635})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.0485572814941406})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.0212461948394775})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 0.9991518259048462})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 39750], ['id', 43510], ['id', 29088], ['id', 56635], ['id', 47659], ['id', 49167], ['id', 17122], ['id', 36117], ['id', 56204], ['id', 3800]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3688048720359802, 0.3661271929740906, 0.35528671741485596, 0.3529602885246277, 0.3496015667915344, 0.346197247505188, 0.3378671407699585, 0.3371332883834839, 0.3361119031906128, 0.335604727268219]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5234375, 'crossentropy': 1.4972834587097168})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5556640625, 'crossentropy': 1.2699083089828491})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1727416515350342})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1244165897369385})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1274032592773438})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1277605295181274})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.255265474319458})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6765, 'crossentropy': 1.1049001953125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.2847172021865845})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.1570712327957153})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.0908077955245972})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.113084077835083})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.024533748626709})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.0706450939178467})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 36519], ['id', 13522], ['id', 13286], ['ood', 56888], ['id', 27124], ['id', 21901], ['id', 4148], ['id', 33596], ['id', 50123], ['id', 27794]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3554954528808594, 0.34868231415748596, 0.32365739345550537, 0.3219571113586426, 0.3191623389720917, 0.3174717426300049, 0.3173021078109741, 0.31538307666778564, 0.31305235624313354, 0.311751127243042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5048828125, 'crossentropy': 1.499407410621643})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.2488045692443848})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1262898445129395})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1091787815093994})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1309876441955566})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1199705600738525})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.2786130905151367})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6779, 'crossentropy': 1.0947283203125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2026475667953491})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.1224534511566162})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.058838129043579})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.0635554790496826})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.06150221824646})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.030124306678772})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 59557], ['id', 33801], ['ood', 7409], ['ood', 25823], ['ood', 59536], ['ood', 36090], ['ood', 40648], ['ood', 50727], ['ood', 14445], ['ood', 34014]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3808116912841797, 0.37273991107940674, 0.36877942085266113, 0.36665916442871094, 0.35645341873168945, 0.35334956645965576, 0.3409985303878784, 0.3397001028060913, 0.3351097106933594, 0.3304402828216553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.46484375, 'crossentropy': 1.528925895690918})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.2249854803085327})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.1468331813812256})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.1366288661956787})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1913180351257324})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2017823457717896})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.263857126235962})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6691, 'crossentropy': 1.10871064453125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.29311203956604})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.1340398788452148})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.11067795753479})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.070192813873291})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.0917994976043701})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.0606681108474731})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 57213], ['id', 31246], ['id', 2782], ['id', 44570], ['id', 53488], ['id', 46995], ['id', 46064], ['id', 12579], ['id', 43793], ['id', 5893]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3750910758972168, 0.3651910424232483, 0.35226142406463623, 0.3397625684738159, 0.3336372375488281, 0.3334267735481262, 0.33163779973983765, 0.33110904693603516, 0.32962489128112793, 0.3245384693145752]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5234375, 'crossentropy': 1.433655023574829})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1875059604644775})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.115902066230774})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1225156784057617})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1474637985229492})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1580191850662231})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6641, 'crossentropy': 1.11036123046875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.297897458076477})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1659293174743652})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.124276041984558})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1109983921051025})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.0849583148956299})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 54078], ['id', 39951], ['id', 37979], ['id', 1342], ['id', 42403], ['id', 57558], ['id', 58915], ['id', 46563], ['id', 33377], ['id', 591]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.31871497631073, 0.30507051944732666, 0.30341458320617676, 0.29031163454055786, 0.2870141267776489, 0.26123321056365967, 0.25994813442230225, 0.25810670852661133, 0.25795412063598633, 0.2571295499801636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5048828125, 'crossentropy': 1.611706018447876})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.2904895544052124})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.1589457988739014})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.117588996887207})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1428718566894531})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1258344650268555})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1958346366882324})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6562, 'crossentropy': 1.131471484375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.2419933080673218})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.180719017982483})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.112147331237793})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.1049070358276367})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.0998508930206299})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.0847896337509155})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 19541], ['id', 30630], ['id', 33232], ['id', 41997], ['id', 34817], ['id', 25899], ['id', 3694], ['id', 13381], ['id', 26960], ['id', 27522]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.33043450117111206, 0.32551050186157227, 0.32490503787994385, 0.3190383315086365, 0.3183867931365967, 0.31735241413116455, 0.31487035751342773, 0.3112870454788208, 0.3100741505622864, 0.30885928869247437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.513671875, 'crossentropy': 1.541062355041504})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.282545566558838})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1573801040649414})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1436238288879395})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1103384494781494})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1560992002487183})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1288037300109863})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1881976127624512})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6697, 'crossentropy': 1.11363359375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.3457436561584473})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1883537769317627})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1467888355255127})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.110227108001709})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.075619101524353})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.0881190299987793})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0685744285583496})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 47870], ['id', 29741], ['id', 2434], ['id', 18584], ['id', 29147], ['ood', 32511], ['id', 52590], ['id', 44], ['id', 17258], ['id', 50815]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.48628348112106323, 0.40457606315612793, 0.403708279132843, 0.4036431908607483, 0.3726918697357178, 0.3722448945045471, 0.37112730741500854, 0.3685307502746582, 0.36438262462615967, 0.35988926887512207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.48828125, 'crossentropy': 1.5385255813598633})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 1.299446702003479})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1696802377700806})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0950260162353516})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0654067993164062})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.063110113143921})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1087818145751953})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1356772184371948})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1659760475158691})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6954, 'crossentropy': 1.0605369140625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2254934310913086})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0989928245544434})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0596474409103394})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0234185457229614})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0284912586212158})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9609941244125366})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 0.9657374620437622})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9429022073745728})
store['active_learning_steps'][32]['eval_training']['best_epoch']=8
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 36843], ['id', 25420], ['id', 7577], ['id', 15226], ['id', 27747], ['id', 15465], ['id', 49891], ['id', 15357], ['id', 19174], ['id', 44873]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4582834839820862, 0.44307368993759155, 0.3973606824874878, 0.37275993824005127, 0.36975938081741333, 0.36813318729400635, 0.361069917678833, 0.35846418142318726, 0.3577115535736084, 0.35643160343170166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5126953125, 'crossentropy': 1.4998888969421387})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.307877779006958})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.2012020349502563})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1312940120697021})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.103142499923706})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1336257457733154})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0734628438949585})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0801652669906616})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.154449224472046})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1399028301239014})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7055, 'crossentropy': 1.0721419921875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.2865211963653564})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.178943157196045})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0654497146606445})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.065306305885315})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0290510654449463})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0112392902374268})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0110303163528442})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0257129669189453})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9940102696418762})
store['active_learning_steps'][33]['eval_training']['best_epoch']=9
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 53513], ['id', 26588], ['id', 22086], ['id', 36538], ['id', 30790], ['id', 30552], ['id', 25397], ['id', 2257], ['id', 52781], ['id', 15389]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4113956093788147, 0.40345919132232666, 0.3959451913833618, 0.3867529034614563, 0.3863679766654968, 0.3684917688369751, 0.367384672164917, 0.36687350273132324, 0.3613860607147217, 0.36038321256637573]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5048828125, 'crossentropy': 1.6068274974822998})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.2461674213409424})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.1581424474716187})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0802533626556396})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0665704011917114})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0785460472106934})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0876691341400146})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1770176887512207})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6869, 'crossentropy': 1.0624306640625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.2763046026229858})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1012964248657227})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.0538606643676758})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0439053773880005})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0170748233795166})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.019822597503662})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0059696435928345})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 19138], ['id', 35859], ['id', 13191], ['id', 44248], ['id', 49886], ['id', 11174], ['id', 22016], ['id', 31683], ['id', 52961], ['id', 29457]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3299332857131958, 0.32340168952941895, 0.3133270740509033, 0.3110473155975342, 0.304792582988739, 0.3011897802352905, 0.30077850818634033, 0.2980365753173828, 0.2952970266342163, 0.29520583152770996]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.4638671875, 'crossentropy': 1.609958529472351})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.2798242568969727})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.144634485244751})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1204140186309814})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0536880493164062})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1290113925933838})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.0734620094299316})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.083847999572754})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6852, 'crossentropy': 1.081465625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.312396764755249})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1856896877288818})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1160448789596558})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1129032373428345})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0441510677337646})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0524463653564453})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0408570766448975})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 36293], ['id', 4436], ['id', 32330], ['id', 21518], ['id', 26823], ['id', 48350], ['id', 36107], ['id', 1344], ['id', 20388], ['id', 9307]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.3312224745750427, 0.3078354597091675, 0.30632448196411133, 0.28667151927948, 0.2865103483200073, 0.28627049922943115, 0.28540658950805664, 0.28479039669036865, 0.284315824508667, 0.2841918468475342]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.5043867826461792})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2198715209960938})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1244409084320068})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0462005138397217})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0346072912216187})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9832941293716431})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0496543645858765})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1449642181396484})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.1270304918289185})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7217, 'crossentropy': 0.99565263671875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.3137328624725342})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1692533493041992})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0785726308822632})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0516259670257568})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.017342209815979})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9861545562744141})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9955819845199585})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9718537926673889})
store['active_learning_steps'][36]['eval_training']['best_epoch']=8
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 6780], ['id', 51418], ['id', 44573], ['id', 37946], ['id', 42521], ['id', 53653], ['id', 44423], ['id', 19550], ['id', 14416], ['id', 37367]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.37768298387527466, 0.3741391897201538, 0.3649117350578308, 0.36169296503067017, 0.3615328073501587, 0.3608796000480652, 0.3563491702079773, 0.3533773422241211, 0.35029715299606323, 0.34978634119033813]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.4921875, 'crossentropy': 1.578047513961792})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.26052987575531})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.0987341403961182})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.116572618484497})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0318957567214966})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0492548942565918})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0391619205474854})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.125553846359253})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6726, 'crossentropy': 1.02526884765625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.323080062866211})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1279325485229492})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.0693714618682861})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0398412942886353})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0456472635269165})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0227347612380981})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.0038130283355713})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 5513], ['id', 21185], ['id', 58708], ['id', 25469], ['id', 41945], ['id', 1925], ['id', 907], ['id', 51708], ['id', 47079], ['id', 31230]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3552556037902832, 0.3248879909515381, 0.3073817491531372, 0.30228060483932495, 0.2949080467224121, 0.28443193435668945, 0.2817617654800415, 0.28147298097610474, 0.2783645987510681, 0.27747642993927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.521484375, 'crossentropy': 1.5512953996658325})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.2839164733886719})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1677641868591309})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.084259271621704})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.114051103591919})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0537887811660767})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0401484966278076})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0311415195465088})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1084257364273071})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.132802963256836})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.0934970378875732})
store['active_learning_steps'][38]['training']['best_epoch']=8
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.7139, 'crossentropy': 1.06750107421875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.305307388305664})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1486804485321045})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.056830644607544})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.07663893699646})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0594916343688965})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 0.9991546869277954})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9674381017684937})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9428166151046753})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9393088817596436})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9232122302055359})
store['active_learning_steps'][38]['eval_training']['best_epoch']=10
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 1776], ['id', 26279], ['id', 22139], ['id', 43346], ['id', 36674], ['id', 34393], ['id', 32909], ['id', 3806], ['id', 43567], ['id', 59691]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4325776696205139, 0.42152130603790283, 0.40813302993774414, 0.3945578336715698, 0.3885278105735779, 0.38609206676483154, 0.38435661792755127, 0.38234078884124756, 0.3821588158607483, 0.3784036636352539]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5107421875, 'crossentropy': 1.5546655654907227})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.2853273153305054})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.157813310623169})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0614171028137207})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.046764850616455})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0085875988006592})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.018730878829956})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0275702476501465})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.048548936843872})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.7141, 'crossentropy': 0.9906556640625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2452492713928223})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.086185336112976})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0857315063476562})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0216639041900635})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0265161991119385})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.026033878326416})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 0.9954784512519836})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9877886176109314})
store['active_learning_steps'][39]['eval_training']['best_epoch']=8
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 58220], ['id', 13482], ['ood', 7222], ['ood', 38466], ['ood', 21618], ['ood', 4900], ['ood', 33706], ['ood', 16204], ['id', 55855], ['id', 24108]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3619006872177124, 0.36075884103775024, 0.3338899612426758, 0.32994329929351807, 0.3286600112915039, 0.3284186124801636, 0.3267495632171631, 0.32673144340515137, 0.3194127678871155, 0.31909382343292236]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.4921875, 'crossentropy': 1.557873249053955})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 1.3533638715744019})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.166260004043579})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1165932416915894})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0341843366622925})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0172746181488037})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0487353801727295})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0643401145935059})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0012246370315552})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1631256341934204})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.2042591571807861})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.2274203300476074})
store['active_learning_steps'][40]['training']['best_epoch']=9
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.7085, 'crossentropy': 1.020396875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.3171595335006714})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1016209125518799})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0278769731521606})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0184271335601807})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9609768390655518})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9605665802955627})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.920587420463562})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9215885996818542})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9179437160491943})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9770184755325317})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9137855768203735})
store['active_learning_steps'][40]['eval_training']['best_epoch']=11
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 30653], ['id', 34303], ['id', 52223], ['id', 54093], ['id', 9771], ['id', 2740], ['id', 40418], ['id', 26160], ['id', 53603], ['id', 32521]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4187609553337097, 0.3534957766532898, 0.35324835777282715, 0.34525609016418457, 0.34271955490112305, 0.34121614694595337, 0.34103453159332275, 0.3405205011367798, 0.3351858854293823, 0.3328545093536377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.494140625, 'crossentropy': 1.5663199424743652})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.2837899923324585})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.1982501745224})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.130447268486023})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0918819904327393})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1002589464187622})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.087780237197876})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0760960578918457})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0892105102539062})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.12625253200531})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1744862794876099})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.7106, 'crossentropy': 1.06531572265625}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.4131025075912476})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1397809982299805})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0486629009246826})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0140297412872314})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0090978145599365})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.9791122674942017})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9801178574562073})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9938421845436096})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9799956679344177})
store['active_learning_steps'][41]['eval_training']['best_epoch']=6
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 23444], ['id', 38613], ['id', 35309], ['id', 26028], ['id', 49545], ['id', 43044], ['id', 56616], ['id', 17595], ['id', 42917], ['id', 17079]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5494579076766968, 0.4717491865158081, 0.4559527635574341, 0.45561492443084717, 0.4435749053955078, 0.44100701808929443, 0.42514538764953613, 0.4246112108230591, 0.42350828647613525, 0.4198944568634033]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.533203125, 'crossentropy': 1.4939112663269043})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.279442310333252})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.217759370803833})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1795158386230469})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1351208686828613})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0575346946716309})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1006807088851929})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0911555290222168})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.2204196453094482})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6875, 'crossentropy': 1.10737099609375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.2795301675796509})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1128997802734375})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0793519020080566})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0548105239868164})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0194694995880127})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0231095552444458})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.034641981124878})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 0.9906842708587646})
store['active_learning_steps'][42]['eval_training']['best_epoch']=8
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 29755], ['id', 27697], ['id', 10381], ['id', 57379], ['id', 39279], ['id', 14408], ['id', 16635], ['id', 46085], ['id', 42300], ['id', 47740]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.47443437576293945, 0.33039093017578125, 0.32846206426620483, 0.3142591714859009, 0.3104017972946167, 0.30741286277770996, 0.3049989938735962, 0.30014568567276, 0.2997540235519409, 0.2970072031021118]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.49609375, 'crossentropy': 1.5775659084320068})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.5576171875, 'crossentropy': 1.232941746711731})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.1685020923614502})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.077580213546753})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0360360145568848})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0101587772369385})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0339460372924805})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.0326533317565918})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0865848064422607})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.7041, 'crossentropy': 1.0303171875}
