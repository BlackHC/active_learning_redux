store = {}
store['timestamp']=1620923680
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=14']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=14
store['worker_id']=14
store['num_workers']=20
store['config']={'seed': 1255, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
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
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 22069], ['id', 2025], ['id', 33382], ['id', 27497], ['id', 16215], ['id', 9068], ['ood', 24968], ['id', 40699], ['ood', 1607], ['id', 42989]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5128698348999023, 0.771967887878418, 0.5858751535415649, 0.5021478533744812, 0.5134621858596802, 0.7981013059616089, 0.6439625024795532, 0.7079685926437378, 0.5896347761154175, 0.840588390827179]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.513371467590332})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.802778959274292})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.9419569969177246})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.0909247398376465})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7187, 'crossentropy': 1.4008943359375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0853934288024902})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0123894214630127})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9953246712684631})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 2627], ['id', 8541], ['id', 28571], ['id', 40560], ['id', 19249], ['id', 44555], ['id', 54587], ['id', 54058], ['id', 37912], ['id', 1410]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5834463834762573, 0.572264552116394, 0.5010424852371216, 0.501102864742279, 0.7224739789962769, 0.5505011081695557, 0.5515350103378296, 0.5011425018310547, 0.47620445489883423, 0.5576299428939819]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.2857320308685303})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.4826385974884033})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.6070160865783691})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.9453589916229248})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.765, 'crossentropy': 1.19634189453125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9890523552894592})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.8244717121124268})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.8609992265701294})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 1285], ['id', 44203], ['id', 4495], ['id', 35375], ['id', 34706], ['id', 41999], ['id', 35499], ['id', 56370], ['ood', 192], ['id', 32080]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5144937038421631, 0.3893618583679199, 0.6365700960159302, 0.49599218368530273, 0.5201119184494019, 0.5566785931587219, 0.5085088610649109, 0.6090119481086731, 0.3586794137954712, 0.41021084785461426]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.134913444519043})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.3610873222351074})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.3773959875106812})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.5642871856689453})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7971, 'crossentropy': 1.06074296875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.8691493272781372})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.830502450466156})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.7862951755523682})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 59400], ['id', 21356], ['id', 44944], ['id', 16580], ['id', 46774], ['id', 41738], ['id', 21659], ['id', 19838], ['id', 49199], ['id', 23771]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5428800582885742, 0.5606337189674377, 0.7103397846221924, 0.45396339893341064, 0.6012428402900696, 0.7767809629440308, 0.2902946472167969, 0.49751681089401245, 0.5948823690414429, 0.58962082862854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0667495727539062})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.2479619979858398})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.4482054710388184})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.3462262153625488})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8008, 'crossentropy': 1.0098494140625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.8614909648895264})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.8320064544677734})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8236527442932129})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 14484], ['id', 29972], ['id', 15735], ['id', 39429], ['id', 37840], ['id', 20916], ['id', 7741], ['id', 32158], ['id', 49983], ['id', 40819]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4714607000350952, 0.5506671667098999, 0.30121558904647827, 0.49879980087280273, 0.33253854513168335, 0.4126437306404114, 0.3674076795578003, 0.4341704845428467, 0.4526083469390869, 0.35736995935440063]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.908903956413269})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.898029088973999})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9091386795043945})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9095110893249512})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9792037010192871})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8679, 'crossentropy': 0.83290634765625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.705133855342865})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6484361886978149})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6013755798339844})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.563650369644165})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
