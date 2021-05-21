store = {}
store['timestamp']=1621471683
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=8']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=8
store['worker_id']=8
store['num_workers']=80
store['config']={'seed': 1242, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.2750072479248047})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.3633909225463867})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.445309638977051})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.7333836555480957})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.669318675994873})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6958, 'crossentropy': 2.172744921875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 11822], ['id', 19423], ['id', 26120], ['id', 59654], ['id', 55531]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.202831243689067, 2.2531922007739533, 3.0691753058507647, 3.6242623503921365, 3.9943896676048993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.222071647644043})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.4650168418884277})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.816183567047119})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.3239262104034424})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.1450181007385254})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.9059157371520996})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.871983051300049})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.728652000427246})
store['active_learning_steps'][1]['training']['best_epoch']=5
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7286, 'crossentropy': 2.044033203125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 7979], ['id', 1981], ['id', 45047], ['id', 23938], ['id', 50090]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1829487420567681, 2.2193327258246813, 3.0565517625713756, 3.655943758872011, 4.024747445485439]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.0235908031463623})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.3296027183532715})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.3649260997772217})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.643998146057129})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.359600782394409})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.4804015159606934})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.626864194869995})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.7784478664398193})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.7525792121887207})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.5718159675598145})
store['active_learning_steps'][2]['training']['best_epoch']=7
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.732, 'crossentropy': 2.5391810546875}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 23190], ['id', 8289], ['id', 15870], ['id', 28371], ['id', 11979]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2892827193624798, 2.4492105176001244, 3.295720927686438, 3.8501728837055147, 4.19756913495774]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.8123173713684082})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.132040023803711})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.3188798427581787})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.552855968475342})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.697117567062378})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.7648472785949707})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7294, 'crossentropy': 2.1959119140625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 33313], ['id', 50716], ['id', 44466], ['id', 37313], ['id', 26577]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1690286721382341, 2.1866203837950087, 3.0185529689670414, 3.6227911786021796, 4.0300557878395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6531059741973877})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.8675998449325562})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.8734445571899414})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.198499917984009})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.195140838623047})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.2368431091308594})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.212625503540039})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.2972278594970703})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.5623090267181396})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.3736047744750977})
store['active_learning_steps'][4]['training']['best_epoch']=7
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.728, 'crossentropy': 2.00096484375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 13030], ['id', 8702], ['id', 31941], ['id', 42383], ['id', 7264]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.2322615460012265, 2.3145736240039314, 3.2037195428216565, 3.808002876378181, 4.160742859282131]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.4670178890228271})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.927986979484558})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.9048985242843628})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.8526239395141602})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.198554277420044})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.3135359287261963})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.468946933746338})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7417, 'crossentropy': 1.8704783203125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 59446], ['id', 32640], ['id', 19972], ['id', 21148], ['id', 42274]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.250329777377437, 2.301767330207814, 3.13300297165868, 3.7329164779505435, 4.109151019340191]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.251235008239746})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.5008513927459717})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.4206457138061523})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.675154209136963})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.795070767402649})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.7801182270050049})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.801, 'crossentropy': 1.2407802734375}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 10244], ['id', 13192], ['id', 13335], ['id', 11617], ['id', 59101]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0749076313320207, 2.0589634908055245, 2.8759015008125104, 3.467343202731957, 3.886190293402139]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.040024757385254})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1425561904907227})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.4230952262878418})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.557039499282837})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.4465579986572266})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7912, 'crossentropy': 1.2189955078125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 36950], ['id', 43126], ['id', 34883], ['id', 3694], ['id', 4646]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0878544250046203, 2.060567850152487, 2.85195272183174, 3.4465082221938674, 3.8557576810169305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.0627267360687256})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.2281324863433838})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.2417151927947998})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.5151526927947998})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.4092119932174683})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.4834100008010864})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.4987921714782715})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.487056016921997})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8195, 'crossentropy': 1.32096142578125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 2826], ['id', 5474], ['id', 15833], ['id', 49064], ['id', 36072]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1883511174259134, 2.180353119675273, 3.009624701564711, 3.6275303821163067, 4.0220470576983995]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.0234862565994263})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0383484363555908})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.2036566734313965})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.1803085803985596})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2855792045593262})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3021817207336426})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3289180994033813})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.4076244831085205})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.84, 'crossentropy': 1.1494451171875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 12903], ['id', 24424], ['id', 17010], ['id', 33222], ['id', 23790]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.1078894524814953, 2.1433252171126513, 2.9859282957490407, 3.6347519353550304, 4.037344098221864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.1281903982162476})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.2539782524108887})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.3099339008331299})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.4980729818344116})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4331321716308594})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.4579399824142456})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.4047036170959473})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.549161434173584})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4763915538787842})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.7155866622924805})
store['active_learning_steps'][10]['training']['best_epoch']=7
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8317, 'crossentropy': 1.2682751953125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 19942], ['id', 50078], ['id', 41911], ['id', 43892], ['id', 12986]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.214511793640593, 2.2513618221241813, 3.120546249300469, 3.745426871492742, 4.124557048676888]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9907582998275757})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0092273950576782})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0804730653762817})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.2038872241973877})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3259971141815186})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8296, 'crossentropy': 0.99633251953125}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 18598], ['id', 57625], ['id', 11096], ['id', 53156], ['id', 5129]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.011828828094723, 1.8987773310334908, 2.6791266551488, 3.2813849870294023, 3.737083426551072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.0266531705856323})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.054806113243103})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9674642086029053})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1079778671264648})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0526254177093506})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1441490650177002})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8495, 'crossentropy': 0.94138447265625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 49890], ['id', 9778], ['id', 57985], ['id', 17121], ['id', 8978]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0705664474709675, 2.058622365810198, 2.9153459268171726, 3.552578344259918, 3.9657006860248636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.9975168704986572})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1806013584136963})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1478397846221924})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2438328266143799})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.230677604675293})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.2764389514923096})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.5350816249847412})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.5746407508850098})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.5453381538391113})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8475, 'crossentropy': 1.20633388671875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 21676], ['id', 42703], ['id', 20641], ['id', 55496], ['id', 42078]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.164190134649982, 2.2452761147102764, 3.1364096063415268, 3.736002098645681, 4.123202500721344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.958804726600647})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.970737099647522})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9535754919052124})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.177302360534668})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0570881366729736})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1216132640838623})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8551, 'crossentropy': 0.93142138671875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 45422], ['id', 14697], ['id', 5536], ['id', 52697], ['id', 11569]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1641840226320244, 2.1855066069926017, 2.971857616124402, 3.579657444627701, 3.9712747281019363]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8873924016952515})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8208422660827637})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8963377475738525})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0012259483337402})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8401, 'crossentropy': 0.873248828125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 20840], ['id', 53504], ['id', 3524], ['id', 59468], ['id', 47787]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6514652460975578, 1.2190517310320939, 1.732459403509404, 2.1813126592130345, 2.580149893673397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.0611553192138672})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8068089485168457})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.822567343711853})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9344791173934937})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9355400204658508})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8579, 'crossentropy': 0.801533251953125}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 22169], ['id', 7990], ['id', 5659], ['id', 33162], ['id', 26966]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.93984727123462, 1.7537600145114798, 2.4790442131201873, 3.0608033711767053, 3.5316817453611415]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9361425638198853})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8860212564468384})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8724715709686279})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9107649922370911})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9487969875335693})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9821422696113586})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9555468559265137})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8607, 'crossentropy': 0.887692578125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 51298], ['id', 9118], ['id', 36409], ['id', 29132], ['id', 6474]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.14473794223772, 2.137943712929514, 2.9527809830173837, 3.563628063180529, 3.9835065984724665]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9199945330619812})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7254443168640137})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8759586811065674})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.863437831401825})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8227911591529846})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8553299903869629})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9941256046295166})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9703525900840759})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1227710247039795})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8774, 'crossentropy': 0.8506654296875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 42774], ['id', 33812], ['id', 44898], ['id', 2845], ['id', 14896]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0645117423618724, 2.0815269006692003, 2.948951491062936, 3.5959511554621013, 4.035346212918013]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.239670753479004})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8297560811042786})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.871719479560852})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9233475923538208})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.104409098625183})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0076881647109985})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8591, 'crossentropy': 0.90328798828125}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 59674], ['id', 644], ['id', 17365], ['id', 11708], ['id', 9332]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.019890496582454, 1.8982506054913584, 2.6666871506544414, 3.2633315134213685, 3.7166509572325257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0172967910766602})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6513465642929077})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6956249475479126})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.70784592628479})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7971675395965576})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.895, 'crossentropy': 0.634278125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 28512], ['id', 2761], ['id', 18324], ['id', 57728], ['id', 52550]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8433996260126855, 1.5839954898360982, 2.2389043211077917, 2.7995728081887874, 3.249387150174634]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9984216690063477})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7018028497695923})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5947360992431641})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7434432506561279})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6722662448883057})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7742140293121338})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9122, 'crossentropy': 0.5826068359375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 57334], ['id', 34520], ['id', 59726], ['id', 32519], ['id', 17849]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.0642115368524632, 2.013922070487124, 2.8229156472434154, 3.441203341140188, 3.851842393213543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.075440764427185})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7298588752746582})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6992647647857666})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.700901985168457})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7152469158172607})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7655653953552246})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9083, 'crossentropy': 0.631933056640625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 25192], ['id', 4784], ['id', 55743], ['id', 46368], ['id', 51426]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9543465108451623, 1.865746750121227, 2.635485136743055, 3.2433128728588887, 3.7056701534954684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.014058232307434})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6227119565010071})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6269848346710205})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.639886736869812})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5881662368774414})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6366785764694214})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6881657838821411})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6952075958251953})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9204, 'crossentropy': 0.55791552734375}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 52940], ['id', 53872], ['id', 19590], ['id', 18003], ['id', 28469]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1137485349367189, 2.098066776365784, 2.9364603297819274, 3.5708522827145153, 3.9855881675929252]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.118948221206665})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6819632649421692})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6268929243087769})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6930078268051147})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7415796518325806})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6885063648223877})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8351324796676636})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8986, 'crossentropy': 0.688124560546875}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 20169], ['id', 35694], ['id', 22053], ['id', 3810], ['id', 22139]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9724221194588158, 1.869188285618287, 2.6446080577795, 3.2678650069959065, 3.7255783813288286]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.132393717765808})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6611511707305908})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6274217963218689})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6584666967391968})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6204590797424316})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6596514582633972})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7855374813079834})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7191827297210693})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9068, 'crossentropy': 0.648378076171875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 45616], ['id', 51508], ['id', 39409], ['id', 2580], ['id', 38698]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0308722981461718, 2.0027214516627296, 2.809165738861373, 3.4428057814891133, 3.879664557276463]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1688624620437622})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.680808424949646})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6289589405059814})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6901204586029053})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.664352536201477})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9014, 'crossentropy': 0.634336376953125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 58560], ['id', 718], ['id', 39818], ['id', 20050], ['id', 29839]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7027056250587449, 1.3398926066665187, 1.9278023735856262, 2.443566579559157, 2.884446534439924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.2336959838867188})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6915346384048462})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6300903558731079})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5774023532867432})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7252923250198364})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6570608615875244})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6904641389846802})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.913, 'crossentropy': 0.56755361328125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 59314], ['id', 23886], ['id', 21692], ['id', 7851], ['id', 26034]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9552199128165137, 1.8442355839804696, 2.6057189546506967, 3.2370057396289873, 3.6906050438665137]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0911883115768433})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6523257493972778})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5890922546386719})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6881438493728638})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.610304594039917})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6104511022567749})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6677383184432983})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6938381195068359})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7150372266769409})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7821688652038574})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9102, 'crossentropy': 0.607558349609375}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 50317], ['id', 29493], ['id', 54388], ['id', 59681], ['id', 53462]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0638977970387364, 2.033783429847713, 2.833995588532291, 3.45193089765731, 3.905674455721628]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.09645676612854})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.666657567024231})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5326210260391235})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5645015239715576})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6429675221443176})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6554087400436401})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.5258853515625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 30884], ['id', 11572], ['id', 58832], ['id', 52099], ['id', 38316]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8711002281337716, 1.685600319710649, 2.4092377685292767, 2.999656450716661, 3.4597856556174804]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2357430458068848})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7292389869689941})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6292704343795776})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6176085472106934})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7317525148391724})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7039108276367188})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8084819912910461})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.721055269241333})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8207563161849976})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9076, 'crossentropy': 0.65250703125}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 42112], ['id', 6269], ['id', 2803], ['id', 45533], ['id', 14341]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.0973053478314831, 2.1264104248660933, 2.9816689159520458, 3.613011461559072, 4.016939934220881]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.2288763523101807})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6959362030029297})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5830837488174438})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.586145281791687})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6194888949394226})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.602470874786377})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7116023302078247})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7132818698883057})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6086437702178955})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6162599325180054})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7550673484802246})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7465828657150269})
store['active_learning_steps'][31]['training']['best_epoch']=9
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.579881640625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 44286], ['id', 16011], ['id', 57211], ['id', 3010], ['id', 10028]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.132489581945251, 2.116602716137719, 2.9352005878486995, 3.5601967402493333, 3.9822637734873485]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2748491764068604})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7145392894744873})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6406316757202148})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6571472883224487})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.71988844871521})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7040829658508301})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6809938549995422})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.797710657119751})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7811441421508789})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8055269122123718})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9101, 'crossentropy': 0.6452755859375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 49826], ['id', 15862], ['id', 7160], ['id', 53054], ['id', 57300]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0498872317775327, 2.0630935774938455, 2.9131152723759914, 3.5539115473804648, 3.986934916374599]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.217261791229248})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6968550682067871})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.540952205657959})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5785224437713623})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6285618543624878})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5919407606124878})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6198092699050903})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9116, 'crossentropy': 0.5510599609375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 37347], ['id', 26072], ['id', 52137], ['id', 6050], ['id', 48360]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9158768018757479, 1.7520235310067314, 2.4849388203823404, 3.0970435261842137, 3.566979566921214]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1762480735778809})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6405631303787231})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5695101022720337})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5158603191375732})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5835208892822266})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5597610473632812})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6178843379020691})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9321, 'crossentropy': 0.46971767578125}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 50370], ['id', 54628], ['id', 46441], ['id', 44661], ['id', 43278]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9057301825383379, 1.7285586996698297, 2.4684251016073944, 3.057014644844948, 3.520094451264411]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.3107331991195679})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6146605014801025})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5645407438278198})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47305911779403687})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4913744628429413})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4867984652519226})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5637956857681274})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9311, 'crossentropy': 0.447784130859375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 8116], ['id', 3691], ['id', 28633], ['id', 22272], ['id', 1674]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.9371493346764941, 1.7553285875150837, 2.44937621096524, 3.041094168236615, 3.5037445899076314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.2273993492126465})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6688377857208252})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.577612042427063})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5784918069839478})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6248229146003723})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5928676724433899})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6332974433898926})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6501942873001099})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6729753017425537})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9223, 'crossentropy': 0.540204296875}
