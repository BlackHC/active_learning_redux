store = {}
store['timestamp']=1620298457
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=21']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=21
store['worker_id']=21
store['num_workers']=40
store['config']={'seed': 22, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4040708541870117})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.8182177543640137})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.8356027603149414})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.934849739074707})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6696, 'crossentropy': 2.2352109375}
store['active_learning_steps'][0]['acquisition']={'indices': [25784, 59854, 23077, 48455, 57698], 'labels': [4, -1, -1, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.0984561443328857})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.4167327880859375})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.6305079460144043})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.83966064453125})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6934, 'crossentropy': 1.85301953125}
store['active_learning_steps'][1]['acquisition']={'indices': [21374, 7481, 24507, 7167, 16983], 'labels': [4, 5, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.814762830734253})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.088150978088379})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.52286434173584})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.5786495208740234})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7234, 'crossentropy': 1.7165173828125}
store['active_learning_steps'][2]['acquisition']={'indices': [43689, 12477, 34137, 29940, 54785], 'labels': [-1, 0, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7943683862686157})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.139383316040039})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.2497119903564453})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.579784393310547})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7184, 'crossentropy': 1.649621484375}
store['active_learning_steps'][3]['acquisition']={'indices': [56974, 7641, 45498, 47200, 44772], 'labels': [3, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.6842079162597656})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.1109800338745117})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.155694007873535})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.3497347831726074})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7517, 'crossentropy': 1.5955330078125}
store['active_learning_steps'][4]['acquisition']={'indices': [5244, 22635, 53273, 27084, 12146], 'labels': [0, 2, 1, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.6244858503341675})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.8947502374649048})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.2946290969848633})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.2121059894561768})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7837, 'crossentropy': 1.377037890625}
store['active_learning_steps'][5]['acquisition']={'indices': [50989, 15649, 7493, 59265, 21340], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.7409629821777344})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.8883496522903442})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 2.159987449645996})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 2.192272186279297})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7608, 'crossentropy': 1.58779091796875}
store['active_learning_steps'][6]['acquisition']={'indices': [37670, 43945, 31651, 58960, 5424], 'labels': [-1, 8, 5, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.5500307083129883})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.7989468574523926})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.8916921615600586})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.12058424949646})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7754, 'crossentropy': 1.38427109375}
store['active_learning_steps'][7]['acquisition']={'indices': [23124, 11754, 12014, 27219, 51278], 'labels': [-1, 0, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.6585818529129028})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.8483824729919434})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 2.1586685180664062})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 2.0104265213012695})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.778, 'crossentropy': 1.43316875}
store['active_learning_steps'][8]['acquisition']={'indices': [13130, 3557, 50062, 1787, 5604], 'labels': [9, 2, 1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.4928646087646484})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.7129838466644287})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.8773717880249023})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.8491430282592773})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7738, 'crossentropy': 1.3071197265625}
store['active_learning_steps'][9]['acquisition']={'indices': [32151, 38415, 52500, 37571, 20093], 'labels': [0, 1, 9, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.3851375579833984})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.8343034982681274})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.9089562892913818})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 2.047745943069458})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7864, 'crossentropy': 1.2921904296875}
store['active_learning_steps'][10]['acquisition']={'indices': [49980, 50685, 37590, 7680, 55896], 'labels': [7, 1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.4848941564559937})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.7411401271820068})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 2.136122226715088})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 2.0562143325805664})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7725, 'crossentropy': 1.3340412109375}
store['active_learning_steps'][11]['acquisition']={'indices': [11161, 3111, 50627, 37119, 30249], 'labels': [-1, 1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.4850287437438965})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.6474456787109375})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.5755884647369385})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.9832007884979248})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7846, 'crossentropy': 1.18947041015625}
store['active_learning_steps'][12]['acquisition']={'indices': [53236, 57108, 46023, 10442, 8304], 'labels': [-1, -1, 9, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.308121919631958})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.5096023082733154})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.5886433124542236})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.946549415588379})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8071, 'crossentropy': 1.13838837890625}
store['active_learning_steps'][13]['acquisition']={'indices': [7326, 18060, 12225, 1574, 6562], 'labels': [-1, 9, -1, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.3330624103546143})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.6307088136672974})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.7506756782531738})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.7030479907989502})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7867, 'crossentropy': 1.21723408203125}
store['active_learning_steps'][14]['acquisition']={'indices': [26932, 17889, 27174, 18208, 38713], 'labels': [2, -1, -1, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.1778016090393066})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.4596128463745117})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.8464982509613037})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.585438847541809})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8022, 'crossentropy': 1.0305349609375}
store['active_learning_steps'][15]['acquisition']={'indices': [2232, 19266, 23760, 53043, 41066], 'labels': [3, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.3118879795074463})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.5230591297149658})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.7085800170898438})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.7155033349990845})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7786, 'crossentropy': 1.19330498046875}
store['active_learning_steps'][16]['acquisition']={'indices': [32919, 19048, 27248, 44158, 22748], 'labels': [8, -1, 3, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.1634728908538818})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.3313319683074951})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.358593463897705})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4943516254425049})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8081, 'crossentropy': 1.0027560546875}
store['active_learning_steps'][17]['acquisition']={'indices': [31008, 45577, 46698, 29500, 5602], 'labels': [-1, 0, -1, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.057307481765747})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.3644561767578125})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2688851356506348})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.6296346187591553})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8138, 'crossentropy': 0.987741796875}
store['active_learning_steps'][18]['acquisition']={'indices': [48749, 33884, 54376, 48180, 46269], 'labels': [6, 4, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.1432099342346191})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.3423683643341064})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.4312622547149658})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.6871137619018555})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7943, 'crossentropy': 1.07933671875}
store['active_learning_steps'][19]['acquisition']={'indices': [27742, 58183, 11398, 5172, 5022], 'labels': [5, 3, -1, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9586099982261658})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1148757934570312})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2780866622924805})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.22292160987854})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8305, 'crossentropy': 0.8865361328125}
store['active_learning_steps'][20]['acquisition']={'indices': [225, 35582, 47671, 38464, 2792], 'labels': [-1, 3, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1511847972869873})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2321515083312988})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.248808741569519})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2712008953094482})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7918, 'crossentropy': 1.0125275390625}
store['active_learning_steps'][21]['acquisition']={'indices': [4027, 56419, 12680, 38581, 12092], 'labels': [-1, 0, 1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.069053053855896})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.3475102186203003})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.252085566520691})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.3429211378097534})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8038, 'crossentropy': 1.00340654296875}
store['active_learning_steps'][22]['acquisition']={'indices': [10752, 19266, 51018, 31950, 52803], 'labels': [-1, 3, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9640319347381592})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1252262592315674})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1151950359344482})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.142906665802002})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8361, 'crossentropy': 0.85905302734375}
store['active_learning_steps'][23]['acquisition']={'indices': [37819, 2576, 1429, 57710, 35507], 'labels': [7, 7, 3, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9709680080413818})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1367642879486084})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2884736061096191})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2157028913497925})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8207, 'crossentropy': 0.91871767578125}
store['active_learning_steps'][24]['acquisition']={'indices': [24172, 25349, 25302, 7659, 43254], 'labels': [-1, 2, 1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9477816820144653})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.977683424949646})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.05924391746521})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.072943925857544})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8331, 'crossentropy': 0.86518623046875}
store['active_learning_steps'][25]['acquisition']={'indices': [35441, 27026, 50645, 58204, 57958], 'labels': [-1, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9400733709335327})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0281469821929932})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2164379358291626})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.164363145828247})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8286, 'crossentropy': 0.8345685546875}
store['active_learning_steps'][26]['acquisition']={'indices': [37965, 40358, 27743, 58023, 30053], 'labels': [-1, 7, 4, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9941787123680115})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0840098857879639})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.195335865020752})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1984883546829224})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8369, 'crossentropy': 0.8770720703125}
store['active_learning_steps'][27]['acquisition']={'indices': [14268, 9856, 13783, 47533, 4893], 'labels': [-1, 1, 5, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8760360479354858})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8488305807113647})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0801547765731812})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.028734803199768})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1017389297485352})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.867, 'crossentropy': 0.768504052734375}
store['active_learning_steps'][28]['acquisition']={'indices': [48900, 37718, 30520, 52216, 50083], 'labels': [-1, 3, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8898210525512695})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9198541045188904})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0943807363510132})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0227352380752563})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8477, 'crossentropy': 0.7926537109375}
store['active_learning_steps'][29]['acquisition']={'indices': [2590, 46147, 44227, 13946, 36537], 'labels': [-1, -1, -1, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8642348051071167})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9493005275726318})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1656309366226196})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.155271291732788})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8288, 'crossentropy': 0.815671875}
store['active_learning_steps'][30]['acquisition']={'indices': [57906, 30118, 51056, 58199, 41119], 'labels': [-1, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8391059637069702})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9095956087112427})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9781584739685059})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1078827381134033})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8474, 'crossentropy': 0.79502880859375}
store['active_learning_steps'][31]['acquisition']={'indices': [25136, 23612, 18591, 55372, 13507], 'labels': [-1, -1, -1, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8996506929397583})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0414263010025024})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9457272887229919})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1387940645217896})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.852, 'crossentropy': 0.8294951171875}
store['active_learning_steps'][32]['acquisition']={'indices': [24468, 28196, 5329, 28855, 54245], 'labels': [9, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.89117431640625})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9457305073738098})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.997056782245636})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.993445873260498})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8487, 'crossentropy': 0.798326953125}
store['active_learning_steps'][33]['acquisition']={'indices': [45447, 52436, 48024, 9363, 16908], 'labels': [6, -1, 1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9283084869384766})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9230304956436157})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.073291540145874})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.129779577255249})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.042093276977539})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8548, 'crossentropy': 0.85901162109375}
store['active_learning_steps'][34]['acquisition']={'indices': [28331, 14281, 39378, 23950, 8184], 'labels': [1, 9, 8, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8634408116340637})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9587396383285522})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.89357990026474})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.075819730758667})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8548, 'crossentropy': 0.8008232421875}
store['active_learning_steps'][35]['acquisition']={'indices': [11744, 40630, 45729, 11943, 56094], 'labels': [4, 0, -1, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8239579200744629})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9547662138938904})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9167433381080627})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.1158819198608398})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8525, 'crossentropy': 0.78298671875}
store['active_learning_steps'][36]['acquisition']={'indices': [55941, 13552, 42026, 25497, 57164], 'labels': [-1, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9611445665359497})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9805266261100769})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0952157974243164})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1966605186462402})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8429, 'crossentropy': 0.84718759765625}
store['active_learning_steps'][37]['acquisition']={'indices': [33405, 55929, 15525, 19326, 42284], 'labels': [7, 8, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9406501054763794})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9186182022094727})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0373594760894775})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1918102502822876})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1309587955474854})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8699, 'crossentropy': 0.80804189453125}
store['active_learning_steps'][38]['acquisition']={'indices': [9103, 32297, 16795, 23325, 9407], 'labels': [-1, 2, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8946840167045593})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9445958137512207})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9555076360702515})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1572206020355225})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8589, 'crossentropy': 0.7763533203125}
store['active_learning_steps'][39]['acquisition']={'indices': [57745, 33779, 4355, 53047, 17980], 'labels': [8, 6, 2, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8941060304641724})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9033536911010742})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0481698513031006})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9402496814727783})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8469, 'crossentropy': 0.776209130859375}
store['active_learning_steps'][40]['acquisition']={'indices': [35607, 51197, 7677, 22822, 58284], 'labels': [6, 1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7749899625778198})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6959949731826782})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9449211359024048})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9944674372673035})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.0204259157180786})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8838, 'crossentropy': 0.693712939453125}
store['active_learning_steps'][41]['acquisition']={'indices': [53858, 56934, 2342, 56690, 19382], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8036023378372192})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8311284184455872})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9569151997566223})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9798712730407715})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8545, 'crossentropy': 0.752435302734375}
store['active_learning_steps'][42]['acquisition']={'indices': [29127, 47149, 21521, 55970, 28959], 'labels': [-1, 7, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8240613341331482})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8898720741271973})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9547260999679565})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9156867265701294})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.86, 'crossentropy': 0.72929765625}
store['active_learning_steps'][43]['acquisition']={'indices': [57843, 2233, 58940, 22871, 45453], 'labels': [0, -1, -1, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8701399564743042})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9150539636611938})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.006543517112732})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0967838764190674})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8561, 'crossentropy': 0.775833984375}
store['active_learning_steps'][44]['acquisition']={'indices': [21795, 48107, 56359, 46098, 15999], 'labels': [3, -1, 7, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8497915267944336})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8957412242889404})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8772724866867065})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9604469537734985})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8635, 'crossentropy': 0.771680615234375}
store['active_learning_steps'][45]['acquisition']={'indices': [29815, 34726, 5265, 1623, 39884], 'labels': [5, -1, 4, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8779531717300415})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8906395435333252})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8257051110267639})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9518966674804688})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0494325160980225})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9738860726356506})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8868, 'crossentropy': 0.79328173828125}
store['active_learning_steps'][46]['acquisition']={'indices': [18538, 43579, 10153, 9181, 10017], 'labels': [0, -1, -1, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7718019485473633})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9165180921554565})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9860610961914062})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.133397102355957})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8506, 'crossentropy': 0.737214111328125}
store['active_learning_steps'][47]['acquisition']={'indices': [8322, 22455, 7934, 45855, 57912], 'labels': [9, 1, -1, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7794027328491211})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8033624887466431})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.895778477191925})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8548732399940491})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8704, 'crossentropy': 0.692802587890625}
store['active_learning_steps'][48]['acquisition']={'indices': [25499, 35998, 53809, 23449, 59613], 'labels': [6, -1, 8, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9149701595306396})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8470041751861572})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.952029824256897})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0194170475006104})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0590872764587402})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8824, 'crossentropy': 0.72970625}
store['active_learning_steps'][49]['acquisition']={'indices': [23136, 18022, 32898, 22015, 17156], 'labels': [-1, 0, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.807746410369873})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8106341361999512})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9327983260154724})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9540829062461853})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8661, 'crossentropy': 0.761729296875}
store['active_learning_steps'][50]['acquisition']={'indices': [39917, 52810, 39768, 42680, 49011], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8570641279220581})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7761805057525635})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8666830062866211})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9424371123313904})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0132555961608887})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8837, 'crossentropy': 0.7175345703125}
store['active_learning_steps'][51]['acquisition']={'indices': [40864, 35469, 28752, 39980, 57699], 'labels': [1, -1, -1, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.829116940498352})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7911794781684875})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7525577545166016})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8371305465698242})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.862630307674408})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9346553087234497})
store['active_learning_steps'][52]['training']['best_epoch']=3
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8933, 'crossentropy': 0.7301025390625}
store['active_learning_steps'][52]['acquisition']={'indices': [27988, 54999, 54534, 56815, 4879], 'labels': [3, 0, 3, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8922388553619385})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8534321784973145})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.965269923210144})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8867321014404297})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9663045406341553})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8746, 'crossentropy': 0.8002720703125}
store['active_learning_steps'][53]['acquisition']={'indices': [18858, 28181, 3565, 28179, 40416], 'labels': [-1, 8, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8515559434890747})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7598346471786499})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9616152048110962})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9971964359283447})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9234559535980225})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8817, 'crossentropy': 0.716807177734375}
store['active_learning_steps'][54]['acquisition']={'indices': [29560, 40855, 26646, 20977, 13729], 'labels': [-1, -1, 2, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8104685544967651})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8507810831069946})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8763182163238525})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8422783613204956})
store['active_learning_steps'][55]['training']['best_epoch']=1
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.878, 'crossentropy': 0.681341455078125}
store['active_learning_steps'][55]['acquisition']={'indices': [36694, 33727, 40965, 53093, 19305], 'labels': [2, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8048996925354004})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8921681642532349})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8423105478286743})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9400641322135925})
store['active_learning_steps'][56]['training']['best_epoch']=1
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8562, 'crossentropy': 0.77952294921875}
store['active_learning_steps'][56]['acquisition']={'indices': [50305, 52206, 45668, 27581, 57139], 'labels': [-1, 6, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9507478475570679})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8172339200973511})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8894308805465698})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9080063104629517})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8968923091888428})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8888, 'crossentropy': 0.69078779296875}
store['active_learning_steps'][57]['acquisition']={'indices': [48737, 8742, 55700, 36648, 2403], 'labels': [8, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8130025863647461})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7889095544815063})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9106993675231934})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8809150457382202})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8634629249572754})
store['active_learning_steps'][58]['training']['best_epoch']=2
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8856, 'crossentropy': 0.6906080078125}
store['active_learning_steps'][58]['acquisition']={'indices': [23336, 12890, 42096, 30138, 52493], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7726926803588867})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.782988965511322})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7095857858657837})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8253505825996399})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.886076807975769})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8932065367698669})
store['active_learning_steps'][59]['training']['best_epoch']=3
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9001, 'crossentropy': 0.64110869140625}
store['active_learning_steps'][59]['acquisition']={'indices': [24011, 25182, 11874, 57129, 38472], 'labels': [0, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8079367876052856})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7618203163146973})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8037416934967041})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8199459314346313})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9068989753723145})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8931, 'crossentropy': 0.65909208984375}
store['active_learning_steps'][60]['acquisition']={'indices': [23338, 14011, 5828, 59056, 49985], 'labels': [3, 7, -1, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7234933376312256})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7387585043907166})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6845948100090027})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8180783987045288})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8608304858207703})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8889992237091064})
store['active_learning_steps'][61]['training']['best_epoch']=3
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8947, 'crossentropy': 0.703914453125}
store['active_learning_steps'][61]['acquisition']={'indices': [14249, 12982, 6046, 37058, 30256], 'labels': [9, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7678514719009399})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6902364492416382})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7328213453292847})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8456370830535889})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8988630175590515})
store['active_learning_steps'][62]['training']['best_epoch']=2
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8949, 'crossentropy': 0.675618798828125}
store['active_learning_steps'][62]['acquisition']={'indices': [25573, 4363, 51508, 22557, 54833], 'labels': [3, 7, 6, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.785175085067749})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7288377285003662})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7513208389282227})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7452795505523682})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8636454939842224})
store['active_learning_steps'][63]['training']['best_epoch']=2
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8892, 'crossentropy': 0.684895263671875}
store['active_learning_steps'][63]['acquisition']={'indices': [53116, 21923, 23345, 43283, 35881], 'labels': [-1, -1, -1, 0, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7328646183013916})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6712567806243896})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7204940915107727})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7307054996490479})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7264325618743896})
store['active_learning_steps'][64]['training']['best_epoch']=2
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8952, 'crossentropy': 0.6336373046875}
store['active_learning_steps'][64]['acquisition']={'indices': [38144, 30363, 54354, 10874, 20607], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.763258695602417})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7490248680114746})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7797110080718994})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.858422040939331})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7964595556259155})
store['active_learning_steps'][65]['training']['best_epoch']=2
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8936, 'crossentropy': 0.648066943359375}
store['active_learning_steps'][65]['acquisition']={'indices': [43780, 53046, 17998, 36465, 3288], 'labels': [5, 5, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7016541957855225})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.807719349861145})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7452987432479858})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8239679336547852})
store['active_learning_steps'][66]['training']['best_epoch']=1
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8724, 'crossentropy': 0.677310302734375}
store['active_learning_steps'][66]['acquisition']={'indices': [45891, 59769, 25442, 17290, 26395], 'labels': [8, 3, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7714495658874512})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7019343376159668})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6663204431533813})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7938765287399292})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.826745867729187})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8731306195259094})
store['active_learning_steps'][67]['training']['best_epoch']=3
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.895, 'crossentropy': 0.664755078125}
store['active_learning_steps'][67]['acquisition']={'indices': [14242, 6029, 18955, 9355, 6658], 'labels': [7, 6, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7186774015426636})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6982340812683105})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7026143074035645})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8087718486785889})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9126927256584167})
store['active_learning_steps'][68]['training']['best_epoch']=2
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8935, 'crossentropy': 0.658172900390625}
store['active_learning_steps'][68]['acquisition']={'indices': [41936, 57875, 42424, 59090, 54874], 'labels': [2, 4, -1, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7767606973648071})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6741193532943726})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8009703755378723})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7873514890670776})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8029831647872925})
store['active_learning_steps'][69]['training']['best_epoch']=2
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8947, 'crossentropy': 0.6322826171875}
store['active_learning_steps'][69]['acquisition']={'indices': [20342, 23159, 9588, 5777, 14648], 'labels': [-1, 9, 7, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7799005508422852})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8032810688018799})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7902349233627319})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7690216302871704})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7740751504898071})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8994267582893372})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7547369599342346})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8583351969718933})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9130216836929321})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.9586226940155029})
store['active_learning_steps'][70]['training']['best_epoch']=7
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.904, 'crossentropy': 0.714318212890625}
store['active_learning_steps'][70]['acquisition']={'indices': [20536, 50298, 50266, 37032, 34825], 'labels': [-1, 0, -1, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7176638841629028})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7320977449417114})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7829763889312744})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7872520685195923})
store['active_learning_steps'][71]['training']['best_epoch']=1
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8772, 'crossentropy': 0.696726513671875}
store['active_learning_steps'][71]['acquisition']={'indices': [15483, 46083, 25274, 43441, 55937], 'labels': [-1, 2, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8074783086776733})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7419514060020447})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7433723211288452})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7773264646530151})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8201385140419006})
store['active_learning_steps'][72]['training']['best_epoch']=2
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8834, 'crossentropy': 0.678362841796875}
store['active_learning_steps'][72]['acquisition']={'indices': [47078, 22845, 41113, 25612, 24430], 'labels': [0, -1, -1, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.796023964881897})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.722234845161438})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8424679040908813})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8399627804756165})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8347184658050537})
store['active_learning_steps'][73]['training']['best_epoch']=2
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.8871, 'crossentropy': 0.6819720703125}
store['active_learning_steps'][73]['acquisition']={'indices': [44883, 10282, 4393, 19288, 34738], 'labels': [-1, -1, -1, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7837811708450317})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7334392070770264})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7568351030349731})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8208057880401611})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.799338698387146})
store['active_learning_steps'][74]['training']['best_epoch']=2
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.8844, 'crossentropy': 0.6542814453125}
store['active_learning_steps'][74]['acquisition']={'indices': [7737, 17888, 41035, 17342, 56151], 'labels': [7, 1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8166497945785522})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6718577146530151})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7242946624755859})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7456187009811401})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.833105206489563})
store['active_learning_steps'][75]['training']['best_epoch']=2
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.8873, 'crossentropy': 0.65934267578125}
store['active_learning_steps'][75]['acquisition']={'indices': [31138, 11347, 44805, 6021, 47955], 'labels': [-1, 6, -1, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7525594234466553})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.683626651763916})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.785173773765564})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.731000542640686})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7649034261703491})
store['active_learning_steps'][76]['training']['best_epoch']=2
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.894, 'crossentropy': 0.630642626953125}
store['active_learning_steps'][76]['acquisition']={'indices': [47580, 59799, 7098, 36904, 12355], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7582024931907654})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6814582943916321})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6658445596694946})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7024145126342773})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6727575063705444})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.75083327293396})
store['active_learning_steps'][77]['training']['best_epoch']=3
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9053, 'crossentropy': 0.605284375}
store['active_learning_steps'][77]['acquisition']={'indices': [45847, 17715, 24372, 29995, 38078], 'labels': [4, -1, 7, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7570165395736694})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6935791969299316})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7379064559936523})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8291951417922974})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8099847435951233})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.8953, 'crossentropy': 0.626746630859375}
store['active_learning_steps'][78]['acquisition']={'indices': [4060, 25121, 56702, 59252, 40022], 'labels': [9, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8186007738113403})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7052551507949829})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7191134691238403})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7521775960922241})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8551430702209473})
store['active_learning_steps'][79]['training']['best_epoch']=2
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.8958, 'crossentropy': 0.666170458984375}
store['active_learning_steps'][79]['acquisition']={'indices': [27752, 58066, 43855, 34206, 17160], 'labels': [2, 4, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7595298290252686})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6422957181930542})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6900683641433716})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7172126770019531})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8195526003837585})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.898, 'crossentropy': 0.5956388671875}
store['active_learning_steps'][80]['acquisition']={'indices': [4329, 27976, 58717, 4364, 25292], 'labels': [9, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6938034296035767})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6989466547966003})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.694526195526123})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7006140947341919})
store['active_learning_steps'][81]['training']['best_epoch']=1
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.8827, 'crossentropy': 0.640704248046875}
store['active_learning_steps'][81]['acquisition']={'indices': [31455, 20842, 55822, 41733, 56940], 'labels': [5, -1, -1, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7816027402877808})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6753978133201599})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6924896240234375})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7151118516921997})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7156881093978882})
store['active_learning_steps'][82]['training']['best_epoch']=2
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9028, 'crossentropy': 0.570333154296875}
store['active_learning_steps'][82]['acquisition']={'indices': [18230, 7039, 21105, 2776, 23419], 'labels': [2, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7044570446014404})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6286947131156921})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6918274164199829})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6595724821090698})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.707007646560669})
store['active_learning_steps'][83]['training']['best_epoch']=2
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9004, 'crossentropy': 0.579453662109375}
store['active_learning_steps'][83]['acquisition']={'indices': [25727, 33240, 8512, 55432, 49933], 'labels': [-1, 3, -1, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6728098392486572})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6397555470466614})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6844295263290405})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6509565114974976})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6371203660964966})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7093466520309448})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6303757429122925})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7077956795692444})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7057700753211975})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8492544889450073})
store['active_learning_steps'][84]['training']['best_epoch']=7
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9222, 'crossentropy': 0.59599013671875}
store['active_learning_steps'][84]['acquisition']={'indices': [40605, 34781, 32791, 43793, 14152], 'labels': [-1, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7018190026283264})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6464403867721558})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7538925409317017})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6714956760406494})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7108032703399658})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9088, 'crossentropy': 0.555231005859375}
store['active_learning_steps'][85]['acquisition']={'indices': [38853, 1908, 33301, 27684, 26932], 'labels': [-1, 3, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7381966710090637})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7516521215438843})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6317417621612549})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6404961347579956})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7279691696166992})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7340801954269409})
store['active_learning_steps'][86]['training']['best_epoch']=3
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9092, 'crossentropy': 0.608449658203125}
store['active_learning_steps'][86]['acquisition']={'indices': [44822, 41873, 21951, 7597, 40920], 'labels': [9, -1, 4, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.750110924243927})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6971394419670105})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6185261011123657})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6856592893600464})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7308785915374756})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7023264169692993})
store['active_learning_steps'][87]['training']['best_epoch']=3
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9119, 'crossentropy': 0.559236376953125}
store['active_learning_steps'][87]['acquisition']={'indices': [31266, 31325, 37502, 543, 12348], 'labels': [-1, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.790737509727478})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7233977317810059})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6759369373321533})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6495169401168823})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6738283634185791})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8013787269592285})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7411280870437622})
store['active_learning_steps'][88]['training']['best_epoch']=4
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9143, 'crossentropy': 0.57856474609375}
store['active_learning_steps'][88]['acquisition']={'indices': [6914, 616, 38368, 35225, 44553], 'labels': [-1, -1, -1, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7097756266593933})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5594834089279175})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6214717626571655})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6504188776016235})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6679841876029968})
store['active_learning_steps'][89]['training']['best_epoch']=2
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9032, 'crossentropy': 0.5583517578125}
store['active_learning_steps'][89]['acquisition']={'indices': [44242, 58594, 43635, 30653, 55753], 'labels': [1, 0, 2, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6419705152511597})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5602203011512756})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5854923129081726})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7178005576133728})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.718487024307251})
store['active_learning_steps'][90]['training']['best_epoch']=2
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9073, 'crossentropy': 0.5224896484375}
store['active_learning_steps'][90]['acquisition']={'indices': [18896, 7553, 29604, 52256, 37515], 'labels': [0, 1, -1, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7152423858642578})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5926377773284912})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6679180264472961})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6845219135284424})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.657915472984314})
store['active_learning_steps'][91]['training']['best_epoch']=2
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.8976, 'crossentropy': 0.583456787109375}
store['active_learning_steps'][91]['acquisition']={'indices': [59729, 56811, 36415, 27943, 19184], 'labels': [8, 6, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7150446176528931})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6805939674377441})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.694668173789978})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6624794006347656})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6777377128601074})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6901484727859497})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7567932605743408})
store['active_learning_steps'][92]['training']['best_epoch']=4
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9085, 'crossentropy': 0.6402986328125}
store['active_learning_steps'][92]['acquisition']={'indices': [50849, 49682, 41644, 16911, 37577], 'labels': [7, -1, -1, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7042403817176819})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5953171253204346})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5663982629776001})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7149490118026733})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6076512336730957})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.7132347226142883})
store['active_learning_steps'][93]['training']['best_epoch']=3
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9161, 'crossentropy': 0.5328923828125}
store['active_learning_steps'][93]['acquisition']={'indices': [34597, 55798, 19742, 24604, 51054], 'labels': [3, -1, -1, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7445740103721619})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5954145193099976})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6266669034957886})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6053584814071655})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6426084041595459})
store['active_learning_steps'][94]['training']['best_epoch']=2
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.8984, 'crossentropy': 0.562925537109375}
store['active_learning_steps'][94]['acquisition']={'indices': [50504, 58950, 8856, 55720, 4761], 'labels': [2, 7, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7215719223022461})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6401287317276001})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.651272177696228})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7178885340690613})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.624148428440094})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6961444020271301})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7224107980728149})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.7222979068756104})
store['active_learning_steps'][95]['training']['best_epoch']=5
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9183, 'crossentropy': 0.6005033203125}
store['active_learning_steps'][95]['acquisition']={'indices': [34386, 24951, 39128, 2950, 56452], 'labels': [7, -1, 4, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7778519988059998})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6053512692451477})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6045898199081421})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6182419061660767})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6516443490982056})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6861060261726379})
store['active_learning_steps'][96]['training']['best_epoch']=3
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9144, 'crossentropy': 0.5509486328125}
store['active_learning_steps'][96]['acquisition']={'indices': [2667, 53952, 13568, 58274, 57520], 'labels': [-1, -1, 3, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7004961967468262})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5558059215545654})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6152889728546143})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6413644552230835})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6535861492156982})
store['active_learning_steps'][97]['training']['best_epoch']=2
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9129, 'crossentropy': 0.518000048828125}
store['active_learning_steps'][97]['acquisition']={'indices': [8814, 25345, 41522, 960, 31977], 'labels': [6, 6, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6740080714225769})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6224366426467896})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5861338376998901})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6257230043411255})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6423234939575195})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.645647406578064})
store['active_learning_steps'][98]['training']['best_epoch']=3
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9161, 'crossentropy': 0.575068359375}
store['active_learning_steps'][98]['acquisition']={'indices': [16451, 37708, 43856, 39882, 48962], 'labels': [9, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6663578748703003})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6128910183906555})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6470641493797302})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.672120213508606})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6981453895568848})
store['active_learning_steps'][99]['training']['best_epoch']=2
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9044, 'crossentropy': 0.568983056640625}
store['active_learning_steps'][99]['acquisition']={'indices': [59379, 47925, 26442, 59926, 43863], 'labels': [-1, 3, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7422186136245728})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.632433295249939})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5885961055755615})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6690801382064819})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6575706005096436})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6568828821182251})
store['active_learning_steps'][100]['training']['best_epoch']=3
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.536394287109375}
store['active_learning_steps'][100]['acquisition']={'indices': [35740, 59643, 43004, 48622, 55360], 'labels': [-1, 3, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7267632484436035})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6390566229820251})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6441302299499512})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6720762252807617})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6083853244781494})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7152236104011536})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7669671773910522})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7006043195724487})
store['active_learning_steps'][101]['training']['best_epoch']=5
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9199, 'crossentropy': 0.567534619140625}
store['active_learning_steps'][101]['acquisition']={'indices': [41273, 55544, 46756, 14298, 32669], 'labels': [-1, 7, 8, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.750717043876648})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5614734888076782})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6266696453094482})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6086571216583252})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6607245802879333})
store['active_learning_steps'][102]['training']['best_epoch']=2
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9162, 'crossentropy': 0.5357275390625}
store['active_learning_steps'][102]['acquisition']={'indices': [10574, 12871, 56747, 55161, 27712], 'labels': [-1, 2, 6, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7082678079605103})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6074707508087158})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5831429362297058})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5443130135536194})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5486232042312622})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6381194591522217})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6422765254974365})
store['active_learning_steps'][103]['training']['best_epoch']=4
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9256, 'crossentropy': 0.501604541015625}
store['active_learning_steps'][103]['acquisition']={'indices': [19664, 5938, 29379, 31155, 452], 'labels': [-1, -1, -1, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7256262302398682})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6082727909088135})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5442653894424438})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.566940426826477})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7254852652549744})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7141627669334412})
store['active_learning_steps'][104]['training']['best_epoch']=3
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9147, 'crossentropy': 0.511628369140625}
store['active_learning_steps'][104]['acquisition']={'indices': [8918, 13656, 12515, 48721, 3146], 'labels': [8, -1, 9, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7317063808441162})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5722696185112})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5602075457572937})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5880923271179199})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6801325082778931})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5816283226013184})
store['active_learning_steps'][105]['training']['best_epoch']=3
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9187, 'crossentropy': 0.497102001953125}
store['active_learning_steps'][105]['acquisition']={'indices': [14332, 3872, 26434, 696, 59217], 'labels': [9, -1, 2, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6829348802566528})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5936064720153809})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5109838247299194})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5584269762039185})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6051433086395264})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6342636346817017})
store['active_learning_steps'][106]['training']['best_epoch']=3
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9267, 'crossentropy': 0.461515283203125}
store['active_learning_steps'][106]['acquisition']={'indices': [6146, 39209, 34706, 29938, 2458], 'labels': [0, 4, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6640057563781738})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5214623808860779})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.591816782951355})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5339467525482178})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6030516624450684})
store['active_learning_steps'][107]['training']['best_epoch']=2
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9179, 'crossentropy': 0.490280224609375}
store['active_learning_steps'][107]['acquisition']={'indices': [13129, 4331, 46839, 36406, 33381], 'labels': [-1, 7, 9, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7061593532562256})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6422802209854126})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5702682733535767})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6774047613143921})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6463419198989868})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6617441773414612})
store['active_learning_steps'][108]['training']['best_epoch']=3
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9123, 'crossentropy': 0.52017294921875}
store['active_learning_steps'][108]['acquisition']={'indices': [38473, 16798, 37255, 5897, 520], 'labels': [-1, 8, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7142810821533203})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5484212636947632})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5578761100769043})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5886096954345703})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5905236005783081})
store['active_learning_steps'][109]['training']['best_epoch']=2
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.911, 'crossentropy': 0.50804697265625}
store['active_learning_steps'][109]['acquisition']={'indices': [27961, 29254, 50653, 39477, 25632], 'labels': [1, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7250036001205444})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5714417695999146})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5892276763916016})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5706281065940857})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6044443845748901})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6284189224243164})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6295169591903687})
store['active_learning_steps'][110]['training']['best_epoch']=4
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9196, 'crossentropy': 0.52645927734375}
store['active_learning_steps'][110]['acquisition']={'indices': [25330, 33273, 27857, 30544, 40305], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6773057579994202})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5787125825881958})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5567322969436646})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6100956201553345})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6196727156639099})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.640609085559845})
store['active_learning_steps'][111]['training']['best_epoch']=3
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9174, 'crossentropy': 0.505044384765625}
store['active_learning_steps'][111]['acquisition']={'indices': [37185, 40421, 58400, 39602, 32030], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6794712543487549})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6663185954093933})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5447939038276672})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5651664733886719})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5941686630249023})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6240732669830322})
store['active_learning_steps'][112]['training']['best_epoch']=3
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9211, 'crossentropy': 0.50479111328125}
store['active_learning_steps'][112]['acquisition']={'indices': [5806, 41879, 46915, 33825, 5893], 'labels': [-1, 1, -1, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6994439363479614})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5631057024002075})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.538800060749054})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5768712162971497})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6480348110198975})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6053987741470337})
store['active_learning_steps'][113]['training']['best_epoch']=3
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.925, 'crossentropy': 0.469967626953125}
store['active_learning_steps'][113]['acquisition']={'indices': [13244, 8145, 39790, 31236, 49730], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6359162330627441})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5668489336967468})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5454388856887817})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.550255537033081})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5815848112106323})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6297333240509033})
store['active_learning_steps'][114]['training']['best_epoch']=3
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9173, 'crossentropy': 0.483456201171875}
store['active_learning_steps'][114]['acquisition']={'indices': [45969, 2653, 54654, 37083, 51825], 'labels': [9, -1, 8, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6774545907974243})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5893198251724243})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6005162596702576})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5676707029342651})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6137019395828247})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7342145442962646})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7393739223480225})
store['active_learning_steps'][115]['training']['best_epoch']=4
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.49755537109375}
store['active_learning_steps'][115]['acquisition']={'indices': [46473, 10402, 21222, 51032, 59468], 'labels': [-1, -1, 7, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6617881059646606})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5625941157341003})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5594677329063416})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5699564218521118})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6065994501113892})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5599928498268127})
store['active_learning_steps'][116]['training']['best_epoch']=3
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.922, 'crossentropy': 0.476632421875}
store['active_learning_steps'][116]['acquisition']={'indices': [11054, 29601, 47058, 30952, 11334], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6532368063926697})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5414386987686157})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5735270977020264})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6340138912200928})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6406490802764893})
store['active_learning_steps'][117]['training']['best_epoch']=2
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9164, 'crossentropy': 0.485222509765625}
store['active_learning_steps'][117]['acquisition']={'indices': [5383, 7787, 54284, 50264, 3646], 'labels': [5, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7118117809295654})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6270455718040466})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5781795382499695})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.567521870136261})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6123809814453125})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6360495090484619})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6844128370285034})
store['active_learning_steps'][118]['training']['best_epoch']=4
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9227, 'crossentropy': 0.49215888671875}
store['active_learning_steps'][118]['acquisition']={'indices': [17064, 11810, 56650, 42275, 10768], 'labels': [-1, 7, 7, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6370599865913391})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.607541561126709})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5915007591247559})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5815544724464417})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5728145837783813})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5885586738586426})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6329324245452881})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6102849245071411})
store['active_learning_steps'][119]['training']['best_epoch']=5
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.9266, 'crossentropy': 0.505348291015625}
store['active_learning_steps'][119]['acquisition']={'indices': [13432, 49043, 6083, 55924, 52700], 'labels': [-1, 6, 1, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6708189249038696})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.49279093742370605})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.550688624382019})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6668946743011475})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.572233259677887})
store['active_learning_steps'][120]['training']['best_epoch']=2
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9173, 'crossentropy': 0.47630341796875}
store['active_learning_steps'][120]['acquisition']={'indices': [19025, 15466, 30573, 48337, 11215], 'labels': [-1, -1, 4, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6563113927841187})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5496597290039062})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5315572619438171})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5757300853729248})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6343393325805664})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6286375522613525})
store['active_learning_steps'][121]['training']['best_epoch']=3
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9232, 'crossentropy': 0.47725244140625}
store['active_learning_steps'][121]['acquisition']={'indices': [20925, 58334, 25914, 51457, 52299], 'labels': [9, 8, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6947510242462158})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.538693368434906})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5418626070022583})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5753066539764404})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6122492551803589})
store['active_learning_steps'][122]['training']['best_epoch']=2
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9188, 'crossentropy': 0.4897361328125}
store['active_learning_steps'][122]['acquisition']={'indices': [21007, 57867, 59039, 24003, 55695], 'labels': [-1, 7, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6654662489891052})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5468474626541138})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5838243961334229})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6447182893753052})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6217433214187622})
store['active_learning_steps'][123]['training']['best_epoch']=2
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.519693603515625}
store['active_learning_steps'][123]['acquisition']={'indices': [3683, 39837, 32632, 20456, 15244], 'labels': [-1, 6, 1, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6513811349868774})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6359534859657288})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5509494543075562})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5946357250213623})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7261977791786194})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6399024724960327})
store['active_learning_steps'][124]['training']['best_epoch']=3
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.924, 'crossentropy': 0.48642333984375}
store['active_learning_steps'][124]['acquisition']={'indices': [53869, 20442, 10120, 11101, 12949], 'labels': [-1, 2, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7528780698776245})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5940886735916138})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5424322485923767})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.559925377368927})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6177691221237183})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5773601531982422})
store['active_learning_steps'][125]['training']['best_epoch']=3
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9228, 'crossentropy': 0.481436767578125}
store['active_learning_steps'][125]['acquisition']={'indices': [14953, 26809, 21071, 46904, 56942], 'labels': [-1, 3, 1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6749188899993896})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5575851202011108})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.530390739440918})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5589991807937622})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6877015829086304})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5891066789627075})
store['active_learning_steps'][126]['training']['best_epoch']=3
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9231, 'crossentropy': 0.47875205078125}
store['active_learning_steps'][126]['acquisition']={'indices': [28088, 18179, 7709, 50099, 3152], 'labels': [9, 1, 0, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6656680107116699})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6000471115112305})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6151263117790222})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5863407850265503})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7073894739151001})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6483173370361328})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6846529245376587})
store['active_learning_steps'][127]['training']['best_epoch']=4
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9255, 'crossentropy': 0.497168701171875}
store['active_learning_steps'][127]['acquisition']={'indices': [40450, 24456, 17004, 38934, 45636], 'labels': [-1, -1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.700289249420166})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5273134708404541})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5382410287857056})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.49778300523757935})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5905338525772095})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5963619947433472})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6184996962547302})
store['active_learning_steps'][128]['training']['best_epoch']=4
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9276, 'crossentropy': 0.459042236328125}
store['active_learning_steps'][128]['acquisition']={'indices': [37685, 49140, 18132, 54875, 7096], 'labels': [-1, 5, -1, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6643796563148499})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5606164932250977})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6275373697280884})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6332504153251648})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6291835904121399})
store['active_learning_steps'][129]['training']['best_epoch']=2
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9181, 'crossentropy': 0.50165556640625}
store['active_learning_steps'][129]['acquisition']={'indices': [57464, 30097, 34799, 50749, 10229], 'labels': [1, -1, 2, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6629960536956787})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5543246269226074})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5441276431083679})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6320609450340271})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5469410419464111})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.578959584236145})
store['active_learning_steps'][130]['training']['best_epoch']=3
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9275, 'crossentropy': 0.471581884765625}
store['active_learning_steps'][130]['acquisition']={'indices': [45075, 36568, 40177, 39035, 58025], 'labels': [-1, 2, -1, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7238078117370605})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5771862864494324})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5587549805641174})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5840238332748413})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5498267412185669})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6134469509124756})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6975213289260864})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6250467896461487})
store['active_learning_steps'][131]['training']['best_epoch']=5
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.928, 'crossentropy': 0.48024443359375}
store['active_learning_steps'][131]['acquisition']={'indices': [56628, 53026, 33106, 6529, 2763], 'labels': [8, 2, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6585164070129395})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5903368592262268})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.49445992708206177})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5341247320175171})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5603493452072144})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5998876094818115})
store['active_learning_steps'][132]['training']['best_epoch']=3
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9243, 'crossentropy': 0.45818583984375}
store['active_learning_steps'][132]['acquisition']={'indices': [53389, 45215, 27826, 11793, 2779], 'labels': [-1, 7, 4, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6873279213905334})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5941038131713867})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5400875210762024})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5290113687515259})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5902522802352905})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6311236619949341})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6155107021331787})
store['active_learning_steps'][133]['training']['best_epoch']=4
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9258, 'crossentropy': 0.492170458984375}
store['active_learning_steps'][133]['acquisition']={'indices': [48802, 38715, 13965, 48618, 55319], 'labels': [9, 2, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6474990248680115})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5490639805793762})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5499314069747925})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5982491970062256})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5420712828636169})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6110882759094238})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5903443694114685})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6305789947509766})
store['active_learning_steps'][134]['training']['best_epoch']=5
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9255, 'crossentropy': 0.491673291015625}
store['active_learning_steps'][134]['acquisition']={'indices': [46366, 1209, 14737, 21047, 55541], 'labels': [5, -1, 5, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.647814154624939})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.555845320224762})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5552893877029419})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5603010654449463})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6445959806442261})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6173518896102905})
store['active_learning_steps'][135]['training']['best_epoch']=3
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.918, 'crossentropy': 0.510587744140625}
store['active_learning_steps'][135]['acquisition']={'indices': [10576, 40619, 30464, 15591, 40700], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.637973427772522})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5212041139602661})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5365654230117798})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5323323011398315})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5669005513191223})
store['active_learning_steps'][136]['training']['best_epoch']=2
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9165, 'crossentropy': 0.468435693359375}
store['active_learning_steps'][136]['acquisition']={'indices': [2614, 32684, 5873, 56238, 14329], 'labels': [-1, -1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6769437789916992})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5170630216598511})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5425465106964111})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5892108678817749})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5934194326400757})
store['active_learning_steps'][137]['training']['best_epoch']=2
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.460362744140625}
store['active_learning_steps'][137]['acquisition']={'indices': [598, 9874, 2701, 2337, 36267], 'labels': [6, -1, -1, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6280702948570251})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.548603355884552})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5461715459823608})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5316539406776428})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6184597015380859})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5715640783309937})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5815693736076355})
store['active_learning_steps'][138]['training']['best_epoch']=4
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9309, 'crossentropy': 0.454714990234375}
store['active_learning_steps'][138]['acquisition']={'indices': [54252, 48540, 8724, 20756, 54306], 'labels': [6, 8, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6484794616699219})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6604410409927368})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5851220488548279})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5591204166412354})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5241818428039551})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5434295535087585})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5990714430809021})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5721824169158936})
store['active_learning_steps'][139]['training']['best_epoch']=5
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9305, 'crossentropy': 0.470068505859375}
store['active_learning_steps'][139]['acquisition']={'indices': [5829, 42951, 58263, 15791, 44536], 'labels': [9, 3, -1, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6782013177871704})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5185914039611816})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.50240558385849})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5481972694396973})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6160224676132202})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5795327425003052})
store['active_learning_steps'][140]['training']['best_epoch']=3
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9319, 'crossentropy': 0.426463818359375}
store['active_learning_steps'][140]['acquisition']={'indices': [37775, 2093, 29739, 57501, 19045], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7298581600189209})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5907137393951416})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5732748508453369})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5975867509841919})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5495353937149048})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5225414037704468})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5727092623710632})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6683101058006287})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5946577191352844})
store['active_learning_steps'][141]['training']['best_epoch']=6
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9331, 'crossentropy': 0.4611251953125}
store['active_learning_steps'][141]['acquisition']={'indices': [51779, 1721, 44576, 26487, 3554], 'labels': [-1, -1, 8, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7207666635513306})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5539733171463013})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5558353662490845})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5304673314094543})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.569120466709137})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6156759262084961})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.591381847858429})
store['active_learning_steps'][142]['training']['best_epoch']=4
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9307, 'crossentropy': 0.441708642578125}
store['active_learning_steps'][142]['acquisition']={'indices': [14918, 47293, 16411, 15890, 47777], 'labels': [-1, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7556476593017578})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5751562118530273})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5286445617675781})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5730941891670227})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5950219631195068})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5772051811218262})
store['active_learning_steps'][143]['training']['best_epoch']=3
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.925, 'crossentropy': 0.463668505859375}
store['active_learning_steps'][143]['acquisition']={'indices': [26823, 23081, 28984, 10661, 12907], 'labels': [5, -1, 9, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.663109540939331})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5312244296073914})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5591920018196106})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5560598373413086})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6299914121627808})
store['active_learning_steps'][144]['training']['best_epoch']=2
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9135, 'crossentropy': 0.499935498046875}
store['active_learning_steps'][144]['acquisition']={'indices': [3659, 50904, 58528, 43625, 20956], 'labels': [2, 5, 7, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6829520463943481})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5556185841560364})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5843794941902161})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5934802293777466})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5291765928268433})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5517070293426514})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5815956592559814})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6376205682754517})
store['active_learning_steps'][145]['training']['best_epoch']=5
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9332, 'crossentropy': 0.457565771484375}
store['active_learning_steps'][145]['acquisition']={'indices': [9416, 52915, 3488, 50863, 23593], 'labels': [7, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.702233076095581})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5644820928573608})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6123549342155457})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5451300144195557})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5380444526672363})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5885353684425354})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5999693870544434})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5674080848693848})
store['active_learning_steps'][146]['training']['best_epoch']=5
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.9292, 'crossentropy': 0.46687314453125}
store['active_learning_steps'][146]['acquisition']={'indices': [42570, 1933, 42133, 52341, 22860], 'labels': [-1, 7, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7679058313369751})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6240712404251099})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6204769611358643})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5958075523376465})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6241031885147095})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6688311100006104})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7087177038192749})
store['active_learning_steps'][147]['training']['best_epoch']=4
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9314, 'crossentropy': 0.46839375}
store['active_learning_steps'][147]['acquisition']={'indices': [29611, 32091, 19260, 1019, 30784], 'labels': [-1, -1, 7, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6394524574279785})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5080511569976807})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5616908073425293})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.512394368648529})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5370262861251831})
store['active_learning_steps'][148]['training']['best_epoch']=2
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9255, 'crossentropy': 0.457184423828125}
store['active_learning_steps'][148]['acquisition']={'indices': [10939, 55254, 45341, 20622, 34619], 'labels': [5, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6576057076454163})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5386242866516113})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.47699928283691406})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5080993175506592})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5282912254333496})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49488765001296997})
store['active_learning_steps'][149]['training']['best_epoch']=3
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.4365888671875}
store['active_learning_steps'][149]['acquisition']={'indices': [11935, 4740, 28081, 50454, 42945], 'labels': [5, 3, 4, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6898593902587891})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.493050217628479})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5553369522094727})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5132536888122559})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5139012336730957})
store['active_learning_steps'][150]['training']['best_epoch']=2
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9175, 'crossentropy': 0.46491513671875}
store['active_learning_steps'][150]['acquisition']={'indices': [27685, 50465, 25541, 28717, 50462], 'labels': [6, -1, -1, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.630864143371582})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.558991551399231})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5400391817092896})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49773579835891724})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5431530475616455})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5629714131355286})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5213399529457092})
store['active_learning_steps'][151]['training']['best_epoch']=4
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9255, 'crossentropy': 0.479904541015625}
store['active_learning_steps'][151]['acquisition']={'indices': [35111, 21335, 41602, 6990, 32564], 'labels': [2, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6878895163536072})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5368768572807312})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5013007521629333})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5479857921600342})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5601102113723755})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5639687776565552})
store['active_learning_steps'][152]['training']['best_epoch']=3
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9303, 'crossentropy': 0.447314501953125}
store['active_learning_steps'][152]['acquisition']={'indices': [5611, 43797, 26200, 22133, 29988], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6797241568565369})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5207953453063965})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.48258882761001587})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5328695774078369})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5804194211959839})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.506693959236145})
store['active_learning_steps'][153]['training']['best_epoch']=3
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.459476123046875}
store['active_learning_steps'][153]['acquisition']={'indices': [5573, 25384, 10790, 19226, 30527], 'labels': [3, 5, 6, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7159162163734436})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.565921425819397})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4868112802505493})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.502017617225647})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5215765237808228})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.49367058277130127})
store['active_learning_steps'][154]['training']['best_epoch']=3
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9291, 'crossentropy': 0.43074599609375}
store['active_learning_steps'][154]['acquisition']={'indices': [33740, 53294, 45384, 57016, 35851], 'labels': [4, 8, 0, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7030128240585327})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5276107788085938})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5306186676025391})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5543157458305359})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.532710075378418})
store['active_learning_steps'][155]['training']['best_epoch']=2
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9222, 'crossentropy': 0.455534375}
store['active_learning_steps'][155]['acquisition']={'indices': [53572, 34314, 10347, 49327, 33055], 'labels': [5, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6441900730133057})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.49262505769729614})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5165328979492188})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5173354744911194})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5414360165596008})
store['active_learning_steps'][156]['training']['best_epoch']=2
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9271, 'crossentropy': 0.4415044921875}
store['active_learning_steps'][156]['acquisition']={'indices': [46002, 406, 52609, 27793, 25397], 'labels': [2, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6952743530273438})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5605511665344238})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5626667141914368})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5847498774528503})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5323099493980408})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5602685213088989})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5795665383338928})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5997653007507324})
store['active_learning_steps'][157]['training']['best_epoch']=5
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9356, 'crossentropy': 0.44623671875}
store['active_learning_steps'][157]['acquisition']={'indices': [7135, 38300, 10105, 32571, 49901], 'labels': [0, -1, 9, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7018060684204102})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5578997731208801})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4668535590171814})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5070540904998779})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5702374577522278})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.480287104845047})
store['active_learning_steps'][158]['training']['best_epoch']=3
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9297, 'crossentropy': 0.417090185546875}
store['active_learning_steps'][158]['acquisition']={'indices': [9236, 38754, 12199, 53152, 19024], 'labels': [-1, 6, 6, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6033324599266052})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5520517826080322})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5516669750213623})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5026907920837402})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5621379613876343})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5015747547149658})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.577091634273529})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.568594753742218})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.596327543258667})
store['active_learning_steps'][159]['training']['best_epoch']=6
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9375, 'crossentropy': 0.437158154296875}
store['active_learning_steps'][159]['acquisition']={'indices': [35418, 9165, 32393, 9622, 20961], 'labels': [-1, 8, 5, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7046276330947876})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5102397203445435})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5118248462677002})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5464794635772705})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5635573863983154})
store['active_learning_steps'][160]['training']['best_epoch']=2
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9176, 'crossentropy': 0.48023828125}
store['active_learning_steps'][160]['acquisition']={'indices': [29976, 44099, 26260, 17057, 41192], 'labels': [-1, 5, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6883174180984497})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5389243960380554})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4982874393463135})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5741952061653137})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6115189790725708})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5604714751243591})
store['active_learning_steps'][161]['training']['best_epoch']=3
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9306, 'crossentropy': 0.42914453125}
store['active_learning_steps'][161]['acquisition']={'indices': [50583, 20066, 4464, 50193, 59425], 'labels': [4, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6175523996353149})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5409641265869141})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4497024118900299})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5353660583496094})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5020288228988647})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4937151074409485})
store['active_learning_steps'][162]['training']['best_epoch']=3
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9266, 'crossentropy': 0.3988758544921875}
store['active_learning_steps'][162]['acquisition']={'indices': [56917, 45982, 37390, 5462, 26029], 'labels': [2, 4, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6080932021141052})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.49988844990730286})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.49676692485809326})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4858284592628479})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5319673418998718})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4998074471950531})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4616767168045044})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5218568444252014})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5547765493392944})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5880477428436279})
store['active_learning_steps'][163]['training']['best_epoch']=7
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9408, 'crossentropy': 0.410628369140625}
store['active_learning_steps'][163]['acquisition']={'indices': [19480, 29947, 59311, 54805, 9428], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6481982469558716})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.48763400316238403})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5070282816886902})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5002497434616089})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5092671513557434})
store['active_learning_steps'][164]['training']['best_epoch']=2
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9284, 'crossentropy': 0.435429443359375}
store['active_learning_steps'][164]['acquisition']={'indices': [36052, 24362, 4498, 59444, 7065], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6546409130096436})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5359187722206116})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5077341198921204})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5323237776756287})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.51198810338974})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5756796598434448})
store['active_learning_steps'][165]['training']['best_epoch']=3
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.419162060546875}
store['active_learning_steps'][165]['acquisition']={'indices': [35261, 25874, 47467, 263, 53263], 'labels': [0, 9, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7056210041046143})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.530890703201294})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5109318494796753})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5676913857460022})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5214225053787231})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5685399770736694})
store['active_learning_steps'][166]['training']['best_epoch']=3
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.423546533203125}
