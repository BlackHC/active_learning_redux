store = {}
store['timestamp']=1620915615
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=14']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=14
store['worker_id']=14
store['num_workers']=20
store['config']={'seed': 1255, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.490886926651001})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.8523449897766113})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8437702655792236})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.2704498767852783})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6499, 'crossentropy': 2.3039515625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2347991466522217})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2812137603759766})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2149622440338135})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [50303, 23347, 823, 10514, 47923, 24409, 11355, 57461, 20903, 56198], 'labels': [6, 8, 8, -1, 0, -1, 8, 5, 3, 3], 'scores': [0.7397975921630859, 0.8419883251190186, 0.5940712690353394, 0.5143367052078247, 0.8449475169181824, 0.5795173645019531, 0.7624603509902954, 0.6931970119476318, 0.9663475751876831, 0.7913315892219543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.9537791013717651})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.087470054626465})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.435028553009033})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.4644718170166016})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7119, 'crossentropy': 1.7393818359375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.1320469379425049})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0501505136489868})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0438406467437744})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [57444, 39942, 43906, 50806, 4901, 35232, 53076, 8411, 38246, 17241], 'labels': [9, 9, 4, 9, 9, 8, 2, 2, 7, 2], 'scores': [0.6939671635627747, 0.8465921878814697, 0.441910982131958, 0.8629284501075745, 0.8686423301696777, 0.5758692026138306, 0.5264654159545898, 0.7795723676681519, 0.6540963053703308, 0.7043365240097046]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.037623882293701})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.6189608573913574})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.7396352291107178})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.7736637592315674})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7018, 'crossentropy': 1.8712091796875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2416718006134033})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1414355039596558})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1219905614852905})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [49568, 40358, 30214, 43452, 24052, 17075, 47115, 23279, 37755, 8749], 'labels': [5, 7, 1, 4, 4, 6, 5, 0, 8, 2], 'scores': [0.6057453155517578, 0.5106201767921448, 0.6672500371932983, 0.6940536499023438, 0.5467862486839294, 0.4631000757217407, 0.709144115447998, 0.5934557914733887, 0.6156362295150757, 0.594102680683136]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.5792510509490967})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 2.0877368450164795})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.1222305297851562})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 2.3403067588806152})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7653, 'crossentropy': 1.42554560546875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.1220734119415283})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.0374486446380615})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.0166051387786865})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [57570, 52247, 10839, 6152, 8555, 13011, 5711, 59214, 37769, 59395], 'labels': [7, 0, 9, 8, 9, 6, 0, 9, 7, 8], 'scores': [0.8222377896308899, 0.6534162759780884, 0.57453453540802, 0.5922937989234924, 0.6643400192260742, 0.6435312032699585, 0.4679843783378601, 0.6105813980102539, 0.827241837978363, 0.5869845747947693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.2620265483856201})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.4756271839141846})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.608302354812622})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.6427278518676758})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7848, 'crossentropy': 1.13194873046875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.8965801000595093})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.8532571196556091})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.8423030376434326})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [23325, 47328, 32308, 12716, 47181, 19904, 39204, 4797, 36796, 45800], 'labels': [2, 8, 4, 0, 7, 7, 4, 8, 7, 9], 'scores': [0.4879874587059021, 0.4253195524215698, 0.36834532022476196, 0.5096609592437744, 0.4003528356552124, 0.555265486240387, 0.4172769784927368, 0.6914620399475098, 0.45222264528274536, 0.4097106456756592]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0978484153747559})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.1772462129592896})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2834187746047974})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.2726917266845703})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8252, 'crossentropy': 0.93524140625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8572402000427246})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.787840723991394})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8008744716644287})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [14476, 40951, 18996, 26405, 19213, 8465, 13096, 14107, 19280, 31404], 'labels': [3, 2, 9, 9, 2, 8, 9, 3, 3, 3], 'scores': [0.41992199420928955, 0.540931761264801, 0.3976708650588989, 0.5476175546646118, 0.552314281463623, 0.5082846879959106, 0.4820341467857361, 0.48185694217681885, 0.4016376733779907, 0.49415791034698486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9891579747200012})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1604810953140259})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1800379753112793})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2046834230422974})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8221, 'crossentropy': 0.90034462890625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.9306178092956543})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8069857358932495})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7681416869163513})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
