store = {}
store['timestamp']=1621034265
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=9']
store['commit']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['github_url']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=9
store['worker_id']=9
store['num_workers']=30
store['config']={'seed': 1246, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.EvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset: FastMNIST (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.499763011932373})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.0954747200012207})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.5772807598114014})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.1594882011413574})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5935, 'crossentropy': 2.6559400390625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.3675611019134521})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.4273873567581177})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.4230914115905762})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 30387], ['ood', 11386], ['ood', 26382], ['ood', 35753], ['ood', 20782], ['ood', 49418], ['ood', 21934], ['ood', 28644], ['ood', 35578], ['ood', 42714]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.1066814661026, 1.0738584995269775, 1.0611103773117065, 1.0573079586029053, 1.0512656569480896, 1.046654760837555, 1.0447090864181519, 1.0417352318763733, 1.037613332271576, 1.036539912223816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 2.093550682067871})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.39033842086792})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.8416342735290527})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.3549399375915527})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5735, 'crossentropy': 2.1204716796875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.3005387783050537})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.251204252243042})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.2249890565872192})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 41131], ['id', 52198], ['id', 2312], ['id', 20150], ['id', 9302], ['id', 50243], ['id', 44903], ['id', 29195], ['id', 55890], ['id', 13717]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7269124388694763, 0.7181149125099182, 0.6917890310287476, 0.6908246874809265, 0.6863082051277161, 0.676243007183075, 0.6736912131309509, 0.6649735569953918, 0.6644972562789917, 0.6607502102851868]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.8531243801116943})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 2.691685676574707})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 3.0892367362976074})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.3678650856018066})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5602, 'crossentropy': 1.9578775390625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.381681203842163})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.3206591606140137})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.3635330200195312})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 37300], ['ood', 28395], ['ood', 46139], ['ood', 7373], ['id', 39169], ['ood', 40335], ['id', 11274], ['ood', 4590], ['ood', 41101], ['ood', 7286]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.48203903436660767, 0.48183321952819824, 0.474875807762146, 0.4578028917312622, 0.45206212997436523, 0.4248976707458496, 0.421292781829834, 0.4210857152938843, 0.4201514720916748, 0.4166097640991211]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.54296875, 'crossentropy': 1.6983025074005127})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.4933013916015625})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.6628284454345703})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.8303933143615723})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5407, 'crossentropy': 1.7801697265625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.3900049924850464})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.3913121223449707})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.4012949466705322})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 9569], ['id', 35292], ['id', 356], ['id', 10384], ['id', 41057], ['id', 10860], ['id', 49197], ['id', 33188], ['id', 53796], ['id', 32550]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.44838929176330566, 0.4069185256958008, 0.40223002433776855, 0.39710021018981934, 0.38979876041412354, 0.3850071430206299, 0.38347291946411133, 0.3792755603790283, 0.3771207332611084, 0.37358272075653076]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.60736083984375})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.3208749294281006})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.3458943367004395})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.9188718795776367})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5579, 'crossentropy': 1.6626384765625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 1.4265663623809814})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.41109299659729})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.3417940139770508})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 44385], ['id', 16530], ['id', 47479], ['id', 5092], ['ood', 3557], ['ood', 59747], ['id', 27479], ['id', 37841], ['id', 9080], ['id', 16853]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.49439454078674316, 0.4917867183685303, 0.4730041027069092, 0.46730077266693115, 0.46217381954193115, 0.4602088928222656, 0.4461146593093872, 0.44314223527908325, 0.43896472454071045, 0.4359610080718994]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.5950483083724976})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.8235595226287842})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.488358974456787})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.397212505340576})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5506, 'crossentropy': 1.58915771484375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.3896386623382568})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5546875, 'crossentropy': 1.360241174697876})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5400390625, 'crossentropy': 1.4074901342391968})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 21901], ['id', 24172], ['id', 2731], ['id', 47164], ['id', 27260], ['id', 21810], ['id', 26791], ['id', 19154], ['id', 14667], ['id', 3947]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.42129504680633545, 0.387336790561676, 0.3582829236984253, 0.3580329418182373, 0.3485010862350464, 0.3482341766357422, 0.3464190363883972, 0.3450585603713989, 0.3449339270591736, 0.34394168853759766]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5283203125, 'crossentropy': 1.566042423248291})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.6720905303955078})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 2.015315294265747})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.6436948776245117})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5308, 'crossentropy': 1.5355205078125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.4853515625, 'crossentropy': 1.470157504081726})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.50390625, 'crossentropy': 1.448296308517456})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5283203125, 'crossentropy': 1.4178006649017334})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 59771], ['id', 37251], ['id', 49891], ['id', 56348], ['id', 30553], ['id', 50397], ['id', 53015], ['id', 59111], ['id', 27090], ['id', 35305]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.35048776865005493, 0.32963597774505615, 0.3144756555557251, 0.31134510040283203, 0.31010520458221436, 0.30620330572128296, 0.3030933141708374, 0.30222153663635254, 0.30107617378234863, 0.3004634380340576]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.3942551612854004})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.5259294509887695})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.616722822189331})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.217405319213867})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5608, 'crossentropy': 1.398182421875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.53125, 'crossentropy': 1.4493526220321655})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.3822755813598633})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5556640625, 'crossentropy': 1.3886802196502686})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 47079], ['id', 24312], ['id', 52509], ['id', 43193], ['id', 46820], ['id', 326], ['id', 26160], ['id', 13286], ['id', 56058], ['id', 24282]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.30412888526916504, 0.2933996915817261, 0.2870464324951172, 0.2841914892196655, 0.27552497386932373, 0.27426213026046753, 0.274153470993042, 0.26567786931991577, 0.2614551782608032, 0.2607992887496948]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5263671875, 'crossentropy': 1.5068702697753906})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.598343849182129})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.8316760063171387})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.0836000442504883})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5108, 'crossentropy': 1.5783181640625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.482421875, 'crossentropy': 1.5577486753463745})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.521484375, 'crossentropy': 1.4735724925994873})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.5263671875, 'crossentropy': 1.4902567863464355})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 37836], ['id', 12241], ['id', 8143], ['id', 4039], ['id', 6036], ['id', 33517], ['id', 56067], ['id', 775], ['id', 25496], ['id', 39766]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.24942028522491455, 0.24647867679595947, 0.24435973167419434, 0.24371099472045898, 0.2429187297821045, 0.24188768863677979, 0.24162757396697998, 0.2406405210494995, 0.24050700664520264, 0.24023652076721191]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.4853515625, 'crossentropy': 1.6165916919708252})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.4364087581634521})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.6182565689086914})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.7096102237701416})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.9354199171066284})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5569, 'crossentropy': 1.42601435546875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.53515625, 'crossentropy': 1.354402780532837})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.51953125, 'crossentropy': 1.3115925788879395})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.2299580574035645})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.541015625, 'crossentropy': 1.2757970094680786})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 52479], ['ood', 46454], ['id', 3800], ['ood', 51717], ['ood', 28303], ['ood', 23144], ['id', 38796], ['ood', 4917], ['ood', 21035], ['ood', 59978]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.33724844455718994, 0.3359854221343994, 0.3281974196434021, 0.31767141819000244, 0.3135807514190674, 0.31333327293395996, 0.3112272024154663, 0.309781551361084, 0.3079935312271118, 0.30715179443359375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.433286428451538})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3359570503234863})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.4455194473266602})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.7279043197631836})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.81913161277771})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.589, 'crossentropy': 1.4013615234375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.2886804342269897})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.2263524532318115})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.2546067237854004})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.206714391708374})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 56978], ['id', 57817], ['id', 12689], ['id', 3293], ['id', 8387], ['id', 16469], ['id', 23425], ['id', 16778], ['id', 21615], ['id', 12188]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.34906089305877686, 0.3095220923423767, 0.3014218807220459, 0.2993457317352295, 0.29816126823425293, 0.2980616092681885, 0.29747098684310913, 0.29711198806762695, 0.2934638261795044, 0.2928593158721924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5185546875, 'crossentropy': 1.5020866394042969})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.4187191724777222})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.6421582698822021})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.8169455528259277})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.8498167991638184})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.5665, 'crossentropy': 1.51480380859375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5, 'crossentropy': 1.3675901889801025})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.2934719324111938})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.2749344110488892})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.2803773880004883})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 52150], ['id', 36674], ['id', 44811], ['id', 42695], ['id', 46657], ['id', 18609], ['id', 55392], ['id', 28745], ['id', 38696], ['id', 49078]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3368809223175049, 0.31590211391448975, 0.31030333042144775, 0.30908286571502686, 0.3073740005493164, 0.30580461025238037, 0.3050485849380493, 0.30470263957977295, 0.3038595914840698, 0.3026866316795349]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.4697265625, 'crossentropy': 1.534224510192871})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.3430233001708984})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.3694337606430054})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.5630826950073242})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.6801574230194092})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.5726, 'crossentropy': 1.40579853515625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5224609375, 'crossentropy': 1.3437864780426025})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.2523479461669922})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 1.2205009460449219})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.2451014518737793})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 27592], ['id', 26568], ['id', 4935], ['id', 36323], ['id', 59671], ['id', 38827], ['id', 1610], ['id', 26044], ['id', 7014], ['id', 14529]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3823283910751343, 0.3606605529785156, 0.35009336471557617, 0.33973228931427, 0.3332800269126892, 0.31958508491516113, 0.3148876428604126, 0.3123852014541626, 0.30979859828948975, 0.3075854778289795]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5048828125, 'crossentropy': 1.4495929479599})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.3936383724212646})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.3477970361709595})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.467423439025879})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.6518852710723877})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.7926554679870605})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.5908, 'crossentropy': 1.4266326171875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.2545111179351807})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.1785318851470947})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.1221184730529785})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.1575126647949219})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.1349016427993774})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 28218], ['id', 39750], ['id', 55765], ['id', 8763], ['id', 30476], ['id', 37650], ['id', 49008], ['id', 32498], ['id', 21258], ['id', 30514]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3679121136665344, 0.3640943765640259, 0.3311469554901123, 0.3258432149887085, 0.30741429328918457, 0.3036816120147705, 0.3031303882598877, 0.3030474781990051, 0.2993791103363037, 0.29410088062286377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.521484375, 'crossentropy': 1.4997003078460693})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3471364974975586})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.390690803527832})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.660414457321167})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.7085275650024414})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.591, 'crossentropy': 1.36162880859375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 1.3488428592681885})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.2525978088378906})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.2822530269622803})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.2048567533493042})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 20581], ['ood', 26533], ['ood', 55997], ['ood', 56065], ['ood', 2855], ['ood', 4071], ['ood', 11319], ['ood', 54075], ['ood', 10417], ['ood', 58581]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.32569098472595215, 0.30770087242126465, 0.29126882553100586, 0.29025590419769287, 0.2790323495864868, 0.27864933013916016, 0.26890671253204346, 0.2668348550796509, 0.2662010192871094, 0.26585566997528076]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5224609375, 'crossentropy': 1.5274434089660645})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.380181908607483})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.416067123413086})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.5759379863739014})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.7566906213760376})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.5847, 'crossentropy': 1.4066259765625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5048828125, 'crossentropy': 1.4040284156799316})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.3338778018951416})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.2846527099609375})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.2841126918792725})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 29501], ['id', 8806], ['id', 25738], ['id', 15290], ['id', 3913], ['id', 45641], ['id', 1770], ['id', 3294], ['id', 44743], ['id', 6207]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.24315428733825684, 0.23662948608398438, 0.23530113697052002, 0.23441612720489502, 0.23438167572021484, 0.22787916660308838, 0.2261582612991333, 0.225044846534729, 0.2249995470046997, 0.22449958324432373]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5107421875, 'crossentropy': 1.5510884523391724})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.29032564163208})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.2677876949310303})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.501589059829712})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.4767024517059326})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.449021816253662})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.61, 'crossentropy': 1.28911953125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.529296875, 'crossentropy': 1.3083572387695312})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.2299628257751465})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.184106469154358})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.1699893474578857})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.169114351272583})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 7671], ['id', 33674], ['id', 27212], ['id', 23648], ['id', 1632], ['id', 17815], ['id', 30408], ['id', 26485], ['id', 26199], ['id', 15143]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.31237244606018066, 0.31096041202545166, 0.29165536165237427, 0.2901902198791504, 0.2830008864402771, 0.27492719888687134, 0.264512836933136, 0.26121872663497925, 0.2610207796096802, 0.26096999645233154]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5029296875, 'crossentropy': 1.642411231994629})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.28425931930542})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.334816336631775})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4505484104156494})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.379089593887329})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.5685, 'crossentropy': 1.32006533203125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.5400390625, 'crossentropy': 1.387278437614441})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.3304436206817627})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.2405154705047607})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.2675700187683105})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 26636], ['id', 1033], ['id', 48494], ['id', 33781], ['ood', 26647], ['id', 46975], ['ood', 18497], ['ood', 4160], ['ood', 24447], ['id', 18018]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.2507683038711548, 0.24822759628295898, 0.24700462818145752, 0.24574649333953857, 0.2390613555908203, 0.2384546995162964, 0.23817121982574463, 0.23803484439849854, 0.23527491092681885, 0.23239773511886597]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.556640625, 'crossentropy': 1.4645583629608154})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2398405075073242})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2329027652740479})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3202896118164062})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.3500697612762451})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.4578344821929932})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6374, 'crossentropy': 1.236078125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.236519694328308})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.143507957458496})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.0942285060882568})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.0854308605194092})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.1074953079223633})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 38613], ['ood', 32776], ['id', 18729], ['id', 54813], ['id', 45262], ['ood', 43404], ['id', 56561], ['id', 22224], ['id', 4219], ['id', 22780]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.37948334217071533, 0.349739670753479, 0.34588301181793213, 0.3405747413635254, 0.3375457525253296, 0.33496272563934326, 0.3342832922935486, 0.327750027179718, 0.3255176544189453, 0.3227041959762573]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5341796875, 'crossentropy': 1.5178552865982056})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.324324131011963})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.2841448783874512})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3088042736053467})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.225500226020813})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.4216430187225342})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.4777641296386719})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.545123815536499})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6459, 'crossentropy': 1.284369140625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.295051097869873})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.216245412826538})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1114401817321777})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1054471731185913})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1124718189239502})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.0855298042297363})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.0701795816421509})
store['active_learning_steps'][19]['eval_training']['best_epoch']=7
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 53522], ['id', 32438], ['id', 56948], ['ood', 27442], ['ood', 11600], ['ood', 11878], ['ood', 38642], ['id', 42362], ['ood', 23020], ['ood', 59390]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5018911361694336, 0.47024446725845337, 0.43171536922454834, 0.42764854431152344, 0.42697829008102417, 0.4180983304977417, 0.41270291805267334, 0.4107765555381775, 0.4098198413848877, 0.4038947820663452]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.505859375, 'crossentropy': 1.5594630241394043})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.3279199600219727})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.2995598316192627})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.303563117980957})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.213975191116333})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.4398114681243896})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.5142230987548828})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.3299800157546997})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.643, 'crossentropy': 1.3256951171875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.2775341272354126})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.1705052852630615})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.1398470401763916})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1169686317443848})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.0624659061431885})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0685136318206787})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.0510817766189575})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 21904], ['id', 55098], ['id', 8879], ['id', 51071], ['id', 39749], ['id', 572], ['id', 12089], ['id', 30851], ['id', 57903], ['id', 43542]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.463759183883667, 0.4439738988876343, 0.4401932954788208, 0.4226332902908325, 0.4172790050506592, 0.408965528011322, 0.408441424369812, 0.4006332755088806, 0.39862358570098877, 0.39681267738342285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.533203125, 'crossentropy': 1.5119636058807373})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.3269422054290771})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2387343645095825})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3317477703094482})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.4130589962005615})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3910393714904785})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6228, 'crossentropy': 1.287414453125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.3068692684173584})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.2235682010650635})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.1934500932693481})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.1536078453063965})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.172486662864685})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 59826], ['id', 35913], ['id', 43346], ['id', 46822], ['id', 58557], ['id', 32462], ['id', 27800], ['id', 42521], ['id', 23077], ['id', 14804]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.33957958221435547, 0.33720648288726807, 0.3173794746398926, 0.3143044710159302, 0.3137372136116028, 0.3086625337600708, 0.3010908365249634, 0.2986534833908081, 0.2963968515396118, 0.29328441619873047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.505859375, 'crossentropy': 1.5137677192687988})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.546875, 'crossentropy': 1.3664207458496094})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.2431752681732178})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.218544840812683})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1951308250427246})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.4335300922393799})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3659186363220215})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.5183477401733398})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6526, 'crossentropy': 1.26038623046875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2023978233337402})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1088957786560059})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0629518032073975})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.0515612363815308})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.069791555404663})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0219718217849731})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0030179023742676})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 49616], ['ood', 38688], ['ood', 54066], ['ood', 52666], ['ood', 29212], ['ood', 50233], ['id', 50272], ['ood', 7033], ['ood', 31699], ['id', 1626]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.44730937480926514, 0.4415903091430664, 0.43757128715515137, 0.4347994327545166, 0.4312208890914917, 0.42741692066192627, 0.4243796467781067, 0.41816413402557373, 0.4179420471191406, 0.41623592376708984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.4326171875, 'crossentropy': 1.6049927473068237})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5068359375, 'crossentropy': 1.346492052078247})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.2810019254684448})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.285144329071045})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3452510833740234})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.5512372255325317})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.5994, 'crossentropy': 1.369110546875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.556640625, 'crossentropy': 1.3763760328292847})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.2595908641815186})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.1883906126022339})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.2316160202026367})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.1951357126235962})
store['active_learning_steps'][23]['eval_training']['best_epoch']=3
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 10920], ['id', 22805], ['id', 29437], ['id', 8689], ['id', 38971], ['id', 32672], ['id', 44125], ['id', 12205], ['id', 56627], ['id', 40092]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.27461057901382446, 0.2730809450149536, 0.2727394104003906, 0.26854097843170166, 0.2654217481613159, 0.26500892639160156, 0.26447439193725586, 0.2607461214065552, 0.26064252853393555, 0.2596006393432617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.48828125, 'crossentropy': 1.5954399108886719})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.529296875, 'crossentropy': 1.293916940689087})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.3297820091247559})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.2638969421386719})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.2847880125045776})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.335580587387085})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4747174978256226})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6036, 'crossentropy': 1.3126396484375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.55078125, 'crossentropy': 1.3519840240478516})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.2065465450286865})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.1898257732391357})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.1141753196716309})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.131793737411499})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.1222515106201172})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 31557], ['id', 6482], ['id', 46064], ['id', 30448], ['id', 48595], ['id', 31627], ['id', 15357], ['id', 17886], ['id', 3457], ['ood', 54729]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.3491605520248413, 0.3427095413208008, 0.3398113250732422, 0.3362250328063965, 0.329551100730896, 0.32146942615509033, 0.3197108507156372, 0.31920039653778076, 0.31313371658325195, 0.3125993013381958]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.4375, 'crossentropy': 1.6473629474639893})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.3259646892547607})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2432959079742432})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4667766094207764})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3207135200500488})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4226360321044922})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6267, 'crossentropy': 1.27997001953125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.5390625, 'crossentropy': 1.366391658782959})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.266244888305664})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.2484431266784668})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2112993001937866})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.1915502548217773})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 20288], ['id', 59775], ['id', 18530], ['id', 16349], ['id', 10718], ['id', 31709], ['id', 13137], ['id', 20138], ['id', 3064], ['id', 3195]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.283322811126709, 0.2781188488006592, 0.2764430046081543, 0.27422475814819336, 0.2728555202484131, 0.27088236808776855, 0.2706284523010254, 0.2692399024963379, 0.26856982707977295, 0.26840507984161377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.4931640625, 'crossentropy': 1.5701638460159302})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.3404884338378906})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.2094087600708008})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.255037784576416})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3489689826965332})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.453752040863037})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.598, 'crossentropy': 1.2775537109375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.5126953125, 'crossentropy': 1.4113318920135498})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.546875, 'crossentropy': 1.238081693649292})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.2261539697647095})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 1.1843112707138062})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.174755573272705})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 16154], ['id', 3806], ['id', 125], ['id', 13598], ['id', 50385], ['id', 32838], ['id', 35971], ['id', 58130], ['id', 12467], ['id', 18814]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3420652151107788, 0.2986832857131958, 0.287601113319397, 0.2850522994995117, 0.28482484817504883, 0.27854758501052856, 0.2758728265762329, 0.2732886075973511, 0.2729288339614868, 0.27216827869415283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5224609375, 'crossentropy': 1.547175407409668})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.324365258216858})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2897511720657349})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2898210287094116})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2531030178070068})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3371453285217285})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.4316176176071167})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.4512276649475098})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6307, 'crossentropy': 1.4177171875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.3533951044082642})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.239542007446289})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.1719293594360352})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.097583532333374})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.167277455329895})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0880035161972046})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.129737138748169})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 36424], ['id', 31612], ['id', 59953], ['id', 33397], ['id', 9227], ['id', 23684], ['id', 12078], ['id', 33311], ['id', 29755], ['id', 46151]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3530730605125427, 0.35287296772003174, 0.3369940519332886, 0.333814799785614, 0.32843613624572754, 0.32785046100616455, 0.3205770254135132, 0.3197687864303589, 0.31966400146484375, 0.3104467988014221]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.4638671875, 'crossentropy': 1.5525269508361816})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.2526795864105225})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.1984702348709106})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1916961669921875})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2073583602905273})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.2935616970062256})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.3037947416305542})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6416, 'crossentropy': 1.221973828125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.3234457969665527})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.220109462738037})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.0971400737762451})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.0920956134796143})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.0962677001953125})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.0795960426330566})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 55459], ['id', 36441], ['id', 27449], ['id', 4915], ['id', 35583], ['id', 1342], ['id', 21716], ['id', 17678], ['id', 53412], ['id', 6594]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3908958435058594, 0.3787045478820801, 0.3656165599822998, 0.3617898225784302, 0.3485509157180786, 0.34804630279541016, 0.334903359413147, 0.32961392402648926, 0.32721590995788574, 0.3248474597930908]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5107421875, 'crossentropy': 1.591493844985962})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.51953125, 'crossentropy': 1.3752875328063965})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.2243366241455078})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1978405714035034})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1675328016281128})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.282435655593872})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2624404430389404})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3455579280853271})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6405, 'crossentropy': 1.23881435546875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.3224457502365112})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.1504533290863037})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.0917308330535889})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.0909998416900635})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1003870964050293})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.0789066553115845})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.0463448762893677})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 55968], ['id', 31853], ['id', 7593], ['id', 27879], ['id', 6571], ['id', 32110], ['id', 41403], ['id', 56551], ['id', 10127], ['id', 26132]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4102233648300171, 0.3747354745864868, 0.37212711572647095, 0.35534369945526123, 0.3492320775985718, 0.34657347202301025, 0.34604954719543457, 0.3394848108291626, 0.3393019437789917, 0.33923280239105225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.4697265625, 'crossentropy': 1.551349401473999})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.187788963317871})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1380623579025269})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1577703952789307})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1659331321716309})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1741480827331543})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6447, 'crossentropy': 1.18055927734375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.53515625, 'crossentropy': 1.3041496276855469})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.1903870105743408})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.087416172027588})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.1229248046875})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.0846457481384277})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 54078], ['ood', 10319], ['id', 9290], ['id', 14410], ['id', 26279], ['id', 5205], ['id', 20624], ['id', 31385], ['id', 15078], ['id', 6389]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3520098924636841, 0.33388543128967285, 0.3222910165786743, 0.30842292308807373, 0.3080408573150635, 0.3036748170852661, 0.29196834564208984, 0.29185783863067627, 0.28882551193237305, 0.28824949264526367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.5065479278564453})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.2923693656921387})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.1630836725234985})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1242567300796509})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1276190280914307})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.117785930633545})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1525673866271973})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1507000923156738})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1634202003479004})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6634, 'crossentropy': 1.17395546875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.2554415464401245})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.139980673789978})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.0678651332855225})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 0.9964970946311951})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0217032432556152})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 0.9837507605552673})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 0.9937415719032288})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.9465406537055969})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 29723], ['id', 5513], ['id', 21185], ['id', 27238], ['id', 36657], ['ood', 39335], ['id', 24079], ['id', 26676], ['id', 43215], ['id', 48293]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4661312699317932, 0.4532052278518677, 0.44859325885772705, 0.44132739305496216, 0.4388818144798279, 0.43468427658081055, 0.422604501247406, 0.41765809059143066, 0.41571909189224243, 0.4095798134803772]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.4453125, 'crossentropy': 1.6695727109909058})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.370445728302002})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.1965548992156982})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0643985271453857})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1015915870666504})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2417006492614746})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.109595775604248})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6586, 'crossentropy': 1.12044541015625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.2722840309143066})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.0960787534713745})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.0748229026794434})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0572431087493896})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.0383949279785156})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1066055297851562})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 35684], ['id', 850], ['id', 58300], ['id', 39483], ['id', 57132], ['id', 27863], ['id', 13841], ['id', 376], ['id', 8953], ['id', 33381]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.2923407554626465, 0.2840200662612915, 0.27647656202316284, 0.2713127136230469, 0.2656916379928589, 0.26460814476013184, 0.26174819469451904, 0.25520873069763184, 0.2541477084159851, 0.2524125576019287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.4921875, 'crossentropy': 1.5457611083984375})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.537109375, 'crossentropy': 1.3097610473632812})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.2443194389343262})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1287339925765991})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.127092957496643})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0598080158233643})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1335198879241943})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1235946416854858})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1117019653320312})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6744, 'crossentropy': 1.107691796875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.3365964889526367})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0731379985809326})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0583544969558716})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.0003777742385864})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0077775716781616})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 0.9725531339645386})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 0.9969087839126587})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9426276683807373})
store['active_learning_steps'][33]['eval_training']['best_epoch']=8
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 33141], ['id', 25420], ['id', 39279], ['id', 43428], ['id', 26986], ['id', 44606], ['id', 44676], ['id', 5374], ['id', 33187], ['id', 7298]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.42181020975112915, 0.3930594325065613, 0.3782658576965332, 0.37236547470092773, 0.36999809741973877, 0.3689364194869995, 0.36598336696624756, 0.3490082025527954, 0.34280598163604736, 0.34201741218566895]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.515625, 'crossentropy': 1.4924218654632568})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 1.2835496664047241})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2082942724227905})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1474403142929077})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0361443758010864})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0775692462921143})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1327440738677979})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.107940435409546})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6889, 'crossentropy': 1.1068326171875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.3271543979644775})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1704168319702148})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0889534950256348})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0733678340911865})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0160595178604126})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0153932571411133})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0223438739776611})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 587], ['id', 7003], ['id', 23295], ['id', 54667], ['id', 37710], ['id', 34952], ['id', 54921], ['id', 1911], ['id', 3410], ['id', 10400]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4020453095436096, 0.4008601903915405, 0.39877182245254517, 0.3689352869987488, 0.3590008020401001, 0.3566465973854065, 0.34925365447998047, 0.3474588394165039, 0.3471256494522095, 0.34688830375671387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.494140625, 'crossentropy': 1.631319284439087})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.267775535583496})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.1630020141601562})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.1777164936065674})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.182307243347168})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1620982885360718})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1521635055541992})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1257972717285156})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1651091575622559})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.3091861009597778})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.308495044708252})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6763, 'crossentropy': 1.2003916015625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.3435955047607422})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.1518616676330566})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.103108286857605})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.0877602100372314})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.0519180297851562})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 0.9895645380020142})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 0.9677729606628418})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 0.9784911870956421})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 0.9671282768249512})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 0.9719091653823853})
store['active_learning_steps'][35]['eval_training']['best_epoch']=9
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 20918], ['id', 35309], ['id', 1935], ['id', 22360], ['id', 50865], ['id', 13568], ['id', 36875], ['id', 49378], ['id', 46563], ['id', 34793]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.46280932426452637, 0.4590498208999634, 0.45185166597366333, 0.4432591199874878, 0.4431501626968384, 0.43866896629333496, 0.4381270408630371, 0.4353755712509155, 0.43354249000549316, 0.43019866943359375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.4794921875, 'crossentropy': 1.6728370189666748})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.54296875, 'crossentropy': 1.3103755712509155})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.2382148504257202})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.1455614566802979})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.128414273262024})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0736303329467773})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0959773063659668})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1175731420516968})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0159764289855957})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0477876663208008})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1739232540130615})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.1789438724517822})
store['active_learning_steps'][36]['training']['best_epoch']=9
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7096, 'crossentropy': 1.09062587890625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.5556640625, 'crossentropy': 1.3317077159881592})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0470598936080933})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.065983772277832})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.005419373512268})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0155316591262817})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 0.9711849689483643})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9440515637397766})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9565412998199463})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9590951204299927})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9315768480300903})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9145420789718628})
store['active_learning_steps'][36]['eval_training']['best_epoch']=11
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 29629], ['id', 20638], ['id', 58220], ['id', 1107], ['id', 25364], ['id', 11862], ['id', 3301], ['id', 32578], ['id', 7315], ['ood', 33124]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4358363151550293, 0.41194748878479004, 0.3962218761444092, 0.39231109619140625, 0.3875768184661865, 0.37560248374938965, 0.3726220726966858, 0.37159186601638794, 0.3708420395851135, 0.3648942708969116]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.4970703125, 'crossentropy': 1.513542652130127})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.2312123775482178})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1891076564788818})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0741429328918457})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1200461387634277})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1325557231903076})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1580688953399658})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6977, 'crossentropy': 1.08227314453125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.3429477214813232})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2264404296875})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.1286654472351074})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.132849931716919})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0589675903320312})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0472595691680908})
store['active_learning_steps'][37]['eval_training']['best_epoch']=6
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 48541], ['id', 55037], ['id', 10052], ['id', 40487], ['id', 15953], ['id', 55576], ['id', 56523], ['id', 54621], ['id', 4618], ['id', 53157]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.2936522960662842, 0.28615617752075195, 0.28270423412323, 0.2786288261413574, 0.2739381790161133, 0.27134406566619873, 0.2690141201019287, 0.2685072422027588, 0.2661244869232178, 0.2654052972793579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.509765625, 'crossentropy': 1.5672669410705566})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.270606279373169})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.1399524211883545})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0496333837509155})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.1046385765075684})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0644598007202148})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9790821075439453})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.047065258026123})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.106380581855774})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.070425271987915})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.7296, 'crossentropy': 0.99203505859375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.3126215934753418})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.0791293382644653})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9875914454460144})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0195512771606445})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 0.9917511940002441})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9390942454338074})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9391160011291504})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9075983762741089})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9132646918296814})
store['active_learning_steps'][38]['eval_training']['best_epoch']=8
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 8919], ['id', 46507], ['id', 13045], ['id', 15274], ['id', 33801], ['id', 6311], ['id', 56860], ['id', 17627], ['id', 12653], ['id', 12587]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.428189754486084, 0.4170161485671997, 0.40502381324768066, 0.401095986366272, 0.39967238903045654, 0.3950842618942261, 0.3866516351699829, 0.3830488324165344, 0.3819845914840698, 0.38022661209106445]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.4951171875, 'crossentropy': 1.5506019592285156})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.55859375, 'crossentropy': 1.2440531253814697})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.1348748207092285})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0901551246643066})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0857470035552979})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0360321998596191})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1671788692474365})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1203522682189941})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0813281536102295})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6981, 'crossentropy': 1.080306640625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.3462588787078857})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.0807912349700928})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.086006760597229})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0271257162094116})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.9613187313079834})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 0.9451005458831787})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9849514961242676})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.8991892337799072})
store['active_learning_steps'][39]['eval_training']['best_epoch']=8
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 33673], ['id', 32330], ['id', 4195], ['ood', 13065], ['id', 49135], ['id', 28543], ['id', 58861], ['id', 11651], ['id', 4701], ['ood', 46524]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.41340911388397217, 0.34337878227233887, 0.34122979640960693, 0.32393312454223633, 0.32006531953811646, 0.31719863414764404, 0.3106435537338257, 0.3098282217979431, 0.3072825074195862, 0.3041543960571289]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.5029296875, 'crossentropy': 1.5802042484283447})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.3188978433609009})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.2001197338104248})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.1537894010543823})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1120047569274902})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.096289873123169})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1608996391296387})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1227777004241943})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1197879314422607})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.675, 'crossentropy': 1.15057822265625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.275200605392456})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.1127643585205078})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.0952409505844116})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.0671026706695557})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0123322010040283})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0018985271453857})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0339956283569336})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.007887601852417})
store['active_learning_steps'][40]['eval_training']['best_epoch']=6
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 12211], ['id', 1882], ['ood', 20635], ['id', 51167], ['ood', 44939], ['id', 57751], ['id', 11251], ['ood', 59657], ['id', 23315], ['id', 5937]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3925051689147949, 0.38358986377716064, 0.381084680557251, 0.3804183006286621, 0.3720203638076782, 0.3708035945892334, 0.368511438369751, 0.3653825521469116, 0.3645104169845581, 0.3637136220932007]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.49609375, 'crossentropy': 1.6359381675720215})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.209652066230774})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.0371122360229492})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0518391132354736})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9664016366004944})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.112727403640747})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1865615844726562})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.133251667022705})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.7079, 'crossentropy': 1.04081845703125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.5400390625, 'crossentropy': 1.3911799192428589})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1375139951705933})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0517404079437256})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 0.9900482892990112})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 0.9528089761734009})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 0.9862923622131348})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9484389424324036})
store['active_learning_steps'][41]['eval_training']['best_epoch']=7
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 34744], ['id', 18414], ['id', 49864], ['id', 40241], ['id', 40742], ['id', 31065], ['id', 50529], ['id', 19362], ['id', 18913], ['id', 27841]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.34680116176605225, 0.33291858434677124, 0.3220837116241455, 0.3194684386253357, 0.318426251411438, 0.3179870843887329, 0.3133622407913208, 0.3055821657180786, 0.3050532937049866, 0.30481207370758057]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.4912109375, 'crossentropy': 1.6129465103149414})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.2794229984283447})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.1475143432617188})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0429797172546387})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.0414756536483765})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0262585878372192})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.074075698852539})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1186902523040771})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1340916156768799})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6944, 'crossentropy': 1.0784693359375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.3159936666488647})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.097036600112915})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.046046257019043})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0468146800994873})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0076452493667603})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.983816385269165})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9579106569290161})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 0.952928900718689})
store['active_learning_steps'][42]['eval_training']['best_epoch']=8
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 17792], ['id', 18584], ['ood', 38106], ['ood', 19832], ['id', 49481], ['id', 5346], ['id', 51511], ['id', 3895], ['id', 9692], ['id', 3830]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3911350965499878, 0.36754149198532104, 0.36735105514526367, 0.36344432830810547, 0.35898923873901367, 0.3583937883377075, 0.3534681797027588, 0.35280895233154297, 0.34654128551483154, 0.34424901008605957]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.521484375, 'crossentropy': 1.6000571250915527})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.2753629684448242})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.0989034175872803})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0875287055969238})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0558607578277588})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0286495685577393})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0378780364990234})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.006506085395813})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9982941150665283})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0321059226989746})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.0307557582855225})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.019897222518921})
store['active_learning_steps'][43]['training']['best_epoch']=9
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.7128, 'crossentropy': 1.08290888671875}
