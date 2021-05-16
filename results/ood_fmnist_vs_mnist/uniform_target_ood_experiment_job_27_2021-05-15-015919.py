store = {}
store['timestamp']=1621040359
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=27']
store['commit']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['github_url']='5f7c992432b59cee0eb3a035912cbb6cccf9ff9a'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=27
store['worker_id']=27
store['num_workers']=30
store['config']={'seed': 1270, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.EvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset: FastMNIST (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.406191825866699})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.055051326751709})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.2179384231567383})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.58992338180542})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5768, 'crossentropy': 2.5758931640625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3007334470748901})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.3782169818878174})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.3682173490524292})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 53803], ['ood', 35472], ['ood', 55024], ['ood', 37945], ['ood', 11567], ['ood', 43634], ['ood', 30311], ['ood', 38557], ['ood', 8644], ['ood', 25260]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.011706531047821, 1.0035839080810547, 0.997488260269165, 0.9973462224006653, 0.9942542910575867, 0.9865992069244385, 0.9864245057106018, 0.9802253842353821, 0.9766284227371216, 0.9747517704963684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.8506097793579102})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.759582996368408})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.1455488204956055})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.6113710403442383})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5885, 'crossentropy': 1.95284375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.2574265003204346})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.2369294166564941})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.2606667280197144})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 50211], ['id', 20946], ['id', 24883], ['id', 24217], ['id', 23416], ['id', 23048], ['id', 15335], ['id', 18860], ['id', 6949], ['id', 33308]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6522240042686462, 0.6511853337287903, 0.6509522795677185, 0.6500640511512756, 0.6400123238563538, 0.6382461190223694, 0.6379872560501099, 0.6260437369346619, 0.6251561045646667, 0.6244124174118042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 2.351198673248291})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 2.947476863861084})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 3.5256752967834473})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.8145508766174316})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5297, 'crossentropy': 2.5687318359375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.54296875, 'crossentropy': 1.5243033170700073})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5478515625, 'crossentropy': 1.5049850940704346})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5478515625, 'crossentropy': 1.5896002054214478})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 7402], ['id', 57620], ['id', 45163], ['id', 12327], ['id', 21935], ['id', 22576], ['id', 35668], ['id', 30927], ['id', 18754], ['id', 2956]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5695788860321045, 0.5624744296073914, 0.5490132570266724, 0.5466874241828918, 0.5393508672714233, 0.5324758291244507, 0.5316255688667297, 0.5234284400939941, 0.5209074020385742, 0.5163662433624268]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.8752834796905518})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.6082725524902344})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.2350871562957764})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 3.07151460647583})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5597, 'crossentropy': 1.863748828125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.3688656091690063})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.3701645135879517})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.3930310010910034})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 7238], ['id', 2502], ['id', 43347], ['id', 19800], ['id', 214], ['id', 16346], ['id', 8374], ['id', 39507], ['id', 37539], ['id', 43727]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.594984233379364, 0.5872299671173096, 0.5659881830215454, 0.5638183355331421, 0.5562953948974609, 0.5529786348342896, 0.540168285369873, 0.5401382446289062, 0.5357774496078491, 0.5319825410842896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.5842092037200928})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.0534071922302246})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 2.7279675006866455})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.420970916748047})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5645, 'crossentropy': 1.567708984375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.3563207387924194})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.3078515529632568})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.265231966972351})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 28733], ['id', 49891], ['id', 887], ['id', 31662], ['id', 28098], ['id', 54813], ['id', 52946], ['id', 30768], ['id', 37709], ['id', 59054]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4515336751937866, 0.38340675830841064, 0.3596358895301819, 0.3554089069366455, 0.3483414649963379, 0.34694623947143555, 0.34472227096557617, 0.34220099449157715, 0.3416574001312256, 0.3392070531845093]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.544921875, 'crossentropy': 1.661954402923584})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 2.089953899383545})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5576171875, 'crossentropy': 2.7455434799194336})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 2.7316200733184814})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5233, 'crossentropy': 1.6677166015625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.494140625, 'crossentropy': 1.4872031211853027})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.52734375, 'crossentropy': 1.4254930019378662})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5205078125, 'crossentropy': 1.42557692527771})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 54196], ['ood', 43960], ['ood', 7286], ['ood', 10363], ['id', 13753], ['ood', 9379], ['ood', 58943], ['ood', 27805], ['ood', 55879], ['ood', 12575]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4627103805541992, 0.43225061893463135, 0.4242173433303833, 0.4196299910545349, 0.4182002544403076, 0.4179494380950928, 0.41259580850601196, 0.4119284152984619, 0.41037899255752563, 0.4058026075363159]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.5591444969177246})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.6947391033172607})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.069192409515381})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.230314254760742})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5182, 'crossentropy': 1.6553787109375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.482421875, 'crossentropy': 1.5656603574752808})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.4951171875, 'crossentropy': 1.5148110389709473})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.455026626586914})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 4689], ['id', 17886], ['id', 39141], ['id', 8985], ['id', 37650], ['id', 54881], ['id', 43510], ['id', 10468], ['id', 1033], ['id', 907]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.478237509727478, 0.438249409198761, 0.43400657176971436, 0.4156094789505005, 0.4116407632827759, 0.39747190475463867, 0.3898463845252991, 0.3881649971008301, 0.3838948607444763, 0.3812074065208435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.4072265625, 'crossentropy': 1.7381408214569092})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.6076829433441162})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 2.026726245880127})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.2610983848571777})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.114189624786377})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5674, 'crossentropy': 1.63295}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.4058260917663574})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.3756837844848633})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.3404994010925293})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.3372721672058105})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 53015], ['ood', 11667], ['ood', 32292], ['id', 14502], ['ood', 22619], ['id', 26518], ['id', 18579], ['id', 28663], ['id', 55392], ['ood', 23241]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4369291067123413, 0.40607213973999023, 0.39118194580078125, 0.3889737129211426, 0.38851267099380493, 0.38609373569488525, 0.3855092525482178, 0.384326696395874, 0.38412904739379883, 0.38326603174209595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.427734375, 'crossentropy': 1.728759765625})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.5891518592834473})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.77004075050354})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.9785513877868652})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.303089141845703})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5355, 'crossentropy': 1.60036171875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.4833984375, 'crossentropy': 1.441629409790039})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.354382872581482})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.319305658340454})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.3092374801635742})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 36138], ['id', 734], ['id', 45557], ['id', 2452], ['id', 59703], ['id', 48083], ['id', 40979], ['id', 23049], ['id', 44782], ['id', 35971]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5228309631347656, 0.4960747957229614, 0.49124211072921753, 0.48190635442733765, 0.461536169052124, 0.45675647258758545, 0.4484739303588867, 0.4470021724700928, 0.43852460384368896, 0.4363059997558594]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.37109375, 'crossentropy': 1.7611372470855713})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.513671875, 'crossentropy': 1.5420284271240234})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.556640625, 'crossentropy': 1.7352943420410156})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.7979086637496948})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.8976929187774658})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5168, 'crossentropy': 1.53126982421875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.478515625, 'crossentropy': 1.470805048942566})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.4892578125, 'crossentropy': 1.3709274530410767})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5087890625, 'crossentropy': 1.3601691722869873})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5234375, 'crossentropy': 1.3391685485839844})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 18276], ['id', 45716], ['id', 57981], ['id', 47079], ['id', 30252], ['id', 4716], ['id', 52223], ['id', 10369], ['id', 35702], ['id', 51188]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.35994720458984375, 0.3440483808517456, 0.3405841588973999, 0.3374946117401123, 0.33328717947006226, 0.33041447401046753, 0.32942354679107666, 0.3274047374725342, 0.324180006980896, 0.3238002061843872]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.3857421875, 'crossentropy': 1.6634869575500488})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.482421875, 'crossentropy': 1.6159782409667969})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.4743576049804688})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.641646146774292})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.7844398021697998})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.012720823287964})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5663, 'crossentropy': 1.564669140625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5048828125, 'crossentropy': 1.4459407329559326})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5205078125, 'crossentropy': 1.306809425354004})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.2783570289611816})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.2587884664535522})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.2561957836151123})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 48668], ['id', 43337], ['id', 59490], ['id', 9297], ['id', 3086], ['id', 23432], ['id', 35874], ['id', 36294], ['id', 8776], ['id', 45306]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5328220725059509, 0.5024991035461426, 0.49445003271102905, 0.4943311810493469, 0.4927734136581421, 0.49263685941696167, 0.4925861954689026, 0.4925404191017151, 0.4909902811050415, 0.49043893814086914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.421875, 'crossentropy': 1.6588996648788452})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.4990234375, 'crossentropy': 1.619150161743164})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 1.568078875541687})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.7061412334442139})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.7176364660263062})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.8208705186843872})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.553, 'crossentropy': 1.5264947265625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.4638671875, 'crossentropy': 1.4751509428024292})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5146484375, 'crossentropy': 1.3541910648345947})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.3070135116577148})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.55078125, 'crossentropy': 1.2910962104797363})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.3124020099639893})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 17744], ['id', 23318], ['id', 27800], ['id', 55765], ['id', 36674], ['id', 4436], ['id', 49008], ['id', 39264], ['id', 35031], ['id', 30872]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4106605052947998, 0.39918214082717896, 0.39541077613830566, 0.38982295989990234, 0.38492661714553833, 0.38212960958480835, 0.38192808628082275, 0.3796457052230835, 0.3793753981590271, 0.3763914108276367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.4091796875, 'crossentropy': 1.6549609899520874})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.490234375, 'crossentropy': 1.520361304283142})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.3805809020996094})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.4119353294372559})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.5718424320220947})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.5327632427215576})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.5912, 'crossentropy': 1.38355478515625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5146484375, 'crossentropy': 1.351682186126709})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.2832331657409668})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5556640625, 'crossentropy': 1.248365044593811})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 1.2089738845825195})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.181074857711792})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 26121], ['id', 50827], ['id', 32266], ['id', 21639], ['id', 39859], ['id', 58519], ['id', 28741], ['id', 28552], ['id', 22868], ['id', 47980]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.42117834091186523, 0.4185175895690918, 0.4184579849243164, 0.4134306311607361, 0.40932977199554443, 0.4074290990829468, 0.40611910820007324, 0.4008709192276001, 0.4008287191390991, 0.3968421220779419]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.4326171875, 'crossentropy': 1.6418192386627197})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5400390625, 'crossentropy': 1.4247496128082275})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 1.4433956146240234})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.5015220642089844})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.474936842918396})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.5143, 'crossentropy': 1.45465302734375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.486328125, 'crossentropy': 1.4548697471618652})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.4697265625, 'crossentropy': 1.4053518772125244})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.4931640625, 'crossentropy': 1.3511662483215332})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.4931640625, 'crossentropy': 1.3618813753128052})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 13598], ['id', 58130], ['id', 8879], ['id', 32110], ['id', 28297], ['id', 59007], ['id', 43241], ['id', 28159], ['id', 8976], ['id', 30476]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3924333453178406, 0.3846622705459595, 0.37757551670074463, 0.37631165981292725, 0.3740888833999634, 0.3738384246826172, 0.37196749448776245, 0.36595630645751953, 0.36558616161346436, 0.3643120527267456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.412109375, 'crossentropy': 1.6764006614685059})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.50390625, 'crossentropy': 1.3672244548797607})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.3129949569702148})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.2987079620361328})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.5499927997589111})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.7783591747283936})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.689753532409668})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6032, 'crossentropy': 1.40946435546875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.350135326385498})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.2210026979446411})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.1856504678726196})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.125007152557373})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.160841464996338})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.1230872869491577})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 53522], ['id', 32438], ['id', 56948], ['id', 47410], ['id', 57947], ['id', 41229], ['id', 2434], ['id', 2799], ['id', 325], ['id', 17751]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4793654680252075, 0.4557170271873474, 0.4541640281677246, 0.4325266480445862, 0.4290432929992676, 0.42268580198287964, 0.4051348567008972, 0.40130728483200073, 0.3936006426811218, 0.3884565234184265]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.4326171875, 'crossentropy': 1.6017780303955078})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5126953125, 'crossentropy': 1.494552731513977})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.3503706455230713})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3997979164123535})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4895495176315308})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.8689594268798828})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.5808, 'crossentropy': 1.45583173828125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5205078125, 'crossentropy': 1.3966400623321533})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.28413987159729})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.2577033042907715})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.2461869716644287})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.2132904529571533})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 33381], ['id', 34311], ['id', 43181], ['id', 29501], ['id', 39707], ['id', 57174], ['id', 57962], ['id', 53654], ['id', 50051], ['id', 52641]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4119234085083008, 0.4115142822265625, 0.3891923427581787, 0.37577950954437256, 0.3731432557106018, 0.37207746505737305, 0.3720289468765259, 0.37100541591644287, 0.36792290210723877, 0.3662078380584717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.478515625, 'crossentropy': 1.4747920036315918})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.3586437702178955})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.2898952960968018})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.401186227798462})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.453728437423706})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.7108230590820312})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.5936, 'crossentropy': 1.32540107421875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.517578125, 'crossentropy': 1.337998390197754})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.5576171875, 'crossentropy': 1.224003791809082})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.2007739543914795})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.168964147567749})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.1766886711120605})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 54215], ['id', 25420], ['id', 56893], ['id', 37507], ['id', 2910], ['id', 36611], ['id', 56503], ['id', 29173], ['id', 6594], ['id', 21869]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.44394630193710327, 0.44286924600601196, 0.43608933687210083, 0.4335431456565857, 0.4264063835144043, 0.41397929191589355, 0.41383326053619385, 0.413510262966156, 0.40831077098846436, 0.40759778022766113]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.4814453125, 'crossentropy': 1.4732487201690674})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.517578125, 'crossentropy': 1.3292516469955444})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.537109375, 'crossentropy': 1.32097589969635})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.3401458263397217})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2360544204711914})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3499566316604614})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.4333155155181885})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.5046463012695312})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.623, 'crossentropy': 1.249641796875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.5263671875, 'crossentropy': 1.3057163953781128})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.1296075582504272})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.1097272634506226})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.1010775566101074})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.0686131715774536})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.0650875568389893})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.0638279914855957})
store['active_learning_steps'][17]['eval_training']['best_epoch']=7
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 32511], ['ood', 58471], ['ood', 41951], ['ood', 46369], ['ood', 57055], ['ood', 15873], ['ood', 20002], ['ood', 6983], ['ood', 8835], ['ood', 15462]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5425636172294617, 0.5339875817298889, 0.48311829566955566, 0.46880948543548584, 0.4654397964477539, 0.46479785442352295, 0.45945751667022705, 0.4508582353591919, 0.44824182987213135, 0.4466656446456909]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.5185546875, 'crossentropy': 1.4156394004821777})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.53515625, 'crossentropy': 1.328676700592041})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.2663462162017822})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.2567843198776245})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3285212516784668})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2439043521881104})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.5385630130767822})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.4116170406341553})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.6880887746810913})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6406, 'crossentropy': 1.29666416015625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.2422233819961548})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.0760793685913086})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.0796127319335938})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.051101565361023})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.015458345413208})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 0.9920122027397156})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.0159962177276611})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 0.9895639419555664})
store['active_learning_steps'][18]['eval_training']['best_epoch']=8
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 15622], ['id', 40453], ['id', 57268], ['id', 15841], ['id', 16154], ['id', 24364], ['id', 70], ['id', 10801], ['id', 16490], ['id', 18482]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4563075304031372, 0.4461127519607544, 0.44181013107299805, 0.44000864028930664, 0.42208755016326904, 0.40485286712646484, 0.40444374084472656, 0.3979198932647705, 0.39663970470428467, 0.39606690406799316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.4755859375, 'crossentropy': 1.4671480655670166})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5390625, 'crossentropy': 1.2863309383392334})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1497379541397095})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.198775053024292})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.232068657875061})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1973605155944824})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6402, 'crossentropy': 1.1621572265625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.478515625, 'crossentropy': 1.3357255458831787})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.2524621486663818})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.1476292610168457})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.1189446449279785})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.0988283157348633})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 55098], ['id', 9924], ['id', 21258], ['id', 11118], ['id', 12689], ['id', 54927], ['id', 2211], ['id', 57297], ['id', 54271], ['id', 53412]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3546481132507324, 0.34624361991882324, 0.332719087600708, 0.3214036822319031, 0.3139159679412842, 0.3131933808326721, 0.3122234344482422, 0.31159257888793945, 0.3106803297996521, 0.3104884624481201]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.4482421875, 'crossentropy': 1.611580729484558})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5205078125, 'crossentropy': 1.3744194507598877})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.1881390810012817})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2095094919204712})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2819030284881592})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3563894033432007})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.5957, 'crossentropy': 1.19035400390625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.51953125, 'crossentropy': 1.2963342666625977})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.525390625, 'crossentropy': 1.208585500717163})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.556640625, 'crossentropy': 1.167079210281372})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.1548793315887451})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.1561801433563232})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 50385], ['id', 51236], ['id', 10181], ['id', 43149], ['id', 26805], ['id', 45171], ['id', 44613], ['id', 5870], ['id', 33503], ['id', 58696]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.354231595993042, 0.3207944631576538, 0.3099042773246765, 0.3063002824783325, 0.30611085891723633, 0.297107458114624, 0.2915419936180115, 0.2870521545410156, 0.2870149612426758, 0.2780085802078247]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.46484375, 'crossentropy': 1.5899755954742432})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 1.311964511871338})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.2823278903961182})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1953723430633545})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2809823751449585})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2479307651519775})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2904839515686035})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6266, 'crossentropy': 1.169629296875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.498046875, 'crossentropy': 1.3222918510437012})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.2187856435775757})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.1525564193725586})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.0961458683013916})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.0767426490783691})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.111112356185913})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 43342], ['id', 56380], ['id', 52150], ['id', 38782], ['id', 3081], ['id', 38613], ['id', 26279], ['id', 36659], ['id', 24108], ['id', 6730]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3611490726470947, 0.357113242149353, 0.3557453155517578, 0.3528980016708374, 0.35116374492645264, 0.34907102584838867, 0.347969114780426, 0.3469091057777405, 0.34448909759521484, 0.3399006128311157]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.4921875, 'crossentropy': 1.470334529876709})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.233818531036377})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2040387392044067})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1362347602844238})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.213515043258667})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2446880340576172})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3281219005584717})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6519, 'crossentropy': 1.18745107421875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.2483274936676025})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.0900590419769287})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.096390962600708})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.080268144607544})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.024726390838623})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.0663292407989502})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 35662], ['id', 48541], ['id', 380], ['id', 17340], ['id', 55576], ['id', 24324], ['id', 59885], ['id', 22949], ['id', 31414], ['id', 54621]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.40989840030670166, 0.407978355884552, 0.4046788215637207, 0.40229332447052, 0.4007977247238159, 0.38456952571868896, 0.3829463720321655, 0.37502431869506836, 0.3744540214538574, 0.3738242983818054]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5244140625, 'crossentropy': 1.4841207265853882})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.2062747478485107})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1976261138916016})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2315237522125244})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1946759223937988})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2764462232589722})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.3712780475616455})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.389174461364746})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6739, 'crossentropy': 1.17830849609375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.2400363683700562})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.0783582925796509})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.068755030632019})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 0.9959037899971008})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 0.9691951870918274})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 0.9544575214385986})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 0.9648690223693848})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 39750], ['id', 46064], ['id', 52967], ['id', 31118], ['id', 16611], ['id', 44434], ['id', 48663], ['id', 52266], ['id', 47256], ['id', 39000]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4559330344200134, 0.42365598678588867, 0.4235835075378418, 0.4043768644332886, 0.40098536014556885, 0.39950668811798096, 0.3987807035446167, 0.39846134185791016, 0.3969654440879822, 0.39301109313964844]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.47265625, 'crossentropy': 1.5005011558532715})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.515625, 'crossentropy': 1.3582236766815186})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.2358033657073975})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1235569715499878})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1651777029037476})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.366036295890808})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.3678945302963257})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6123, 'crossentropy': 1.1612005859375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.5205078125, 'crossentropy': 1.2407982349395752})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.5517578125, 'crossentropy': 1.1114367246627808})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.0923817157745361})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.0989047288894653})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.0432381629943848})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.0289427042007446})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 19138], ['id', 15119], ['id', 996], ['id', 47728], ['id', 51402], ['id', 21960], ['id', 39951], ['id', 24953], ['ood', 50479], ['id', 9291]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3338804244995117, 0.3118119239807129, 0.2984832525253296, 0.29810214042663574, 0.29552721977233887, 0.29527556896209717, 0.2942376732826233, 0.2929004430770874, 0.29115772247314453, 0.2905740737915039]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5234375, 'crossentropy': 1.4531478881835938})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.2163978815078735})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.1482616662979126})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.1928377151489258})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.2425837516784668})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.225014567375183})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6117, 'crossentropy': 1.1587578125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.3625597953796387})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.1625072956085205})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.176563024520874})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.1481971740722656})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.1125191450119019})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 40742], ['id', 1031], ['id', 9862], ['id', 39766], ['id', 30985], ['ood', 38716], ['id', 19174], ['id', 51071], ['ood', 37631], ['id', 18584]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3157769441604614, 0.30973100662231445, 0.2859210968017578, 0.28537750244140625, 0.2804844379425049, 0.27881932258605957, 0.2781400680541992, 0.27630048990249634, 0.26967954635620117, 0.26862382888793945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5029296875, 'crossentropy': 1.4759138822555542})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5302734375, 'crossentropy': 1.3228896856307983})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.2554560899734497})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.1921954154968262})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.1707803010940552})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2270689010620117})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3437334299087524})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2355695962905884})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6274, 'crossentropy': 1.2091240234375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.285510778427124})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.1246974468231201})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.0984517335891724})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.0483460426330566})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.077174186706543})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.0401886701583862})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.0384289026260376})
store['active_learning_steps'][26]['eval_training']['best_epoch']=7
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 7782], ['ood', 9658], ['ood', 5684], ['id', 13995], ['id', 35309], ['ood', 35691], ['ood', 20581], ['id', 57751], ['id', 31827], ['id', 38806]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3920307159423828, 0.3573373556137085, 0.34952545166015625, 0.34943991899490356, 0.34838414192199707, 0.3477308750152588, 0.34735918045043945, 0.3452962040901184, 0.34421205520629883, 0.34380435943603516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.4873046875, 'crossentropy': 1.5513222217559814})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.517578125, 'crossentropy': 1.3418151140213013})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.1949553489685059})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2128729820251465})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2287441492080688})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2742189168930054})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.623, 'crossentropy': 1.146845703125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.53125, 'crossentropy': 1.384002447128296})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.2278785705566406})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 1.199838638305664})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.1859278678894043})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.1451359987258911})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 58560], ['id', 3301], ['id', 26462], ['id', 35305], ['id', 12078], ['id', 30274], ['id', 18913], ['id', 43193], ['id', 37710], ['id', 37824]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3193380832672119, 0.3076653480529785, 0.2969837188720703, 0.291179895401001, 0.28927361965179443, 0.2782973051071167, 0.26794910430908203, 0.2659587860107422, 0.2613520622253418, 0.26022887229919434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.451171875, 'crossentropy': 1.6488533020019531})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.3527023792266846})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.2178364992141724})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1748056411743164})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2789490222930908})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2224488258361816})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1435900926589966})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2172940969467163})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3466696739196777})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3009083271026611})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6607, 'crossentropy': 1.17153857421875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.3402700424194336})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.113125205039978})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.080885410308838})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0349525213241577})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.0183402299880981})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.0355308055877686})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.0155208110809326})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0014458894729614})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.0315682888031006})
store['active_learning_steps'][28]['eval_training']['best_epoch']=8
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 59105], ['id', 37251], ['id', 52949], ['ood', 49616], ['id', 33645], ['id', 21904], ['id', 30001], ['id', 6389], ['id', 28628], ['ood', 50930]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4239112138748169, 0.4140433073043823, 0.4028923511505127, 0.4014045000076294, 0.39754772186279297, 0.3962951898574829, 0.3937748670578003, 0.39087367057800293, 0.3908272385597229, 0.38611340522766113]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.498046875, 'crossentropy': 1.5649439096450806})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.310794711112976})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.2287025451660156})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.2691047191619873})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.2340233325958252})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.339330792427063})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.5614, 'crossentropy': 1.30163662109375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.5205078125, 'crossentropy': 1.4310779571533203})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.533203125, 'crossentropy': 1.3234288692474365})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.2575340270996094})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.5478515625, 'crossentropy': 1.2573686838150024})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.537109375, 'crossentropy': 1.240462303161621})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 50665], ['id', 37695], ['id', 16530], ['id', 59145], ['id', 54667], ['id', 9683], ['id', 37658], ['id', 6818], ['id', 42521], ['id', 49267]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.3063797950744629, 0.29312968254089355, 0.2899181842803955, 0.28781330585479736, 0.2846202850341797, 0.28379952907562256, 0.28054118156433105, 0.28002381324768066, 0.2797278165817261, 0.2790783643722534]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5302734375, 'crossentropy': 1.5128000974655151})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.284684658050537})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.2436778545379639})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1479763984680176})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.181056261062622})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2953228950500488})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.234961986541748})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6316, 'crossentropy': 1.15273505859375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.5498046875, 'crossentropy': 1.357308030128479})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.1536085605621338})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1282122135162354})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.0619370937347412})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.078185796737671})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.0781586170196533})
store['active_learning_steps'][30]['eval_training']['best_epoch']=4
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 44540], ['id', 56978], ['id', 50962], ['id', 3459], ['id', 58636], ['id', 19362], ['id', 3219], ['id', 44251], ['id', 58729], ['id', 54981]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.33814847469329834, 0.33780789375305176, 0.3377997875213623, 0.3375577926635742, 0.33556580543518066, 0.3329273462295532, 0.33171510696411133, 0.3287769556045532, 0.3285442590713501, 0.326346755027771]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.4765625, 'crossentropy': 1.6050710678100586})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.556640625, 'crossentropy': 1.3001506328582764})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.256075382232666})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2176648378372192})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2418031692504883})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.3338979482650757})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.323390007019043})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6319, 'crossentropy': 1.20659013671875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.2999658584594727})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.1606489419937134})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.159334421157837})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.168165683746338})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.0894900560379028})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.0604877471923828})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 15078], ['id', 57213], ['id', 7577], ['id', 4703], ['ood', 31787], ['ood', 2998], ['ood', 57948], ['ood', 14753], ['ood', 33648], ['ood', 54210]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.33519482612609863, 0.32807886600494385, 0.3242766857147217, 0.32295429706573486, 0.3211268186569214, 0.3100268840789795, 0.30903124809265137, 0.3086596727371216, 0.307722806930542, 0.30767810344696045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.4580078125, 'crossentropy': 1.5767067670822144})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.3526170253753662})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.2370684146881104})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.2190442085266113})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.1811543703079224})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.210158348083496})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2798688411712646})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2178547382354736})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.642, 'crossentropy': 1.20987197265625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.3887648582458496})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.1769087314605713})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.1536190509796143})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.1328284740447998})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.1142845153808594})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.0925909280776978})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.083648443222046})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 33141], ['id', 54405], ['id', 23345], ['id', 25813], ['id', 4191], ['id', 57306], ['id', 10548], ['id', 50745], ['id', 30815], ['id', 326]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3686422109603882, 0.36244916915893555, 0.34893798828125, 0.3482096195220947, 0.3392183780670166, 0.334403395652771, 0.33374857902526855, 0.33308959007263184, 0.32602035999298096, 0.3248162865638733]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.484375, 'crossentropy': 1.5378230810165405})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.3205125331878662})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.1940613985061646})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.32893705368042})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1969943046569824})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2244929075241089})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.594, 'crossentropy': 1.20050087890625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.396789789199829})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.5556640625, 'crossentropy': 1.295424461364746})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.24861478805542})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.2085351943969727})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.2017529010772705})
store['active_learning_steps'][33]['eval_training']['best_epoch']=5
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 35684], ['id', 39279], ['id', 30901], ['id', 59771], ['id', 2113], ['id', 17191], ['id', 3913], ['id', 1344], ['id', 47112], ['id', 26636]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.2987043857574463, 0.29751014709472656, 0.2874026298522949, 0.286812424659729, 0.28658461570739746, 0.2862190008163452, 0.2795943021774292, 0.2788124084472656, 0.27379631996154785, 0.2730731964111328]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 1.5239148139953613})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.2670488357543945})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.1387618780136108})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1015880107879639})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.059150218963623})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.194807529449463})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.25497305393219})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.193248987197876})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6565, 'crossentropy': 1.09162255859375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.2715661525726318})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.1609915494918823})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1035186052322388})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.0722510814666748})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.0254743099212646})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.0283117294311523})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.0529747009277344})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 51163], ['id', 24014], ['id', 125], ['id', 3009], ['id', 29277], ['id', 51167], ['id', 17463], ['id', 50158], ['id', 9461], ['id', 35336]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4167952537536621, 0.3461877107620239, 0.3308302164077759, 0.3228048086166382, 0.32092952728271484, 0.3178689479827881, 0.3169867992401123, 0.3167227506637573, 0.3128776550292969, 0.2997084856033325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.515625, 'crossentropy': 1.5271246433258057})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.2052639722824097})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.2090301513671875})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1218698024749756})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.0613666772842407})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1534614562988281})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1496577262878418})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1013844013214111})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6687, 'crossentropy': 1.0851625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.3882908821105957})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.156139850616455})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.063429594039917})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.022895097732544})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.0462841987609863})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.0465466976165771})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0319384336471558})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 20624], ['id', 33596], ['id', 58379], ['id', 42243], ['id', 33673], ['id', 18670], ['id', 34753], ['id', 53776], ['id', 52509], ['id', 41350]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.33274614810943604, 0.3140387535095215, 0.3077828884124756, 0.3075554370880127, 0.30368030071258545, 0.299258828163147, 0.29392480850219727, 0.29276156425476074, 0.2916758060455322, 0.289595365524292]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.546875, 'crossentropy': 1.5386614799499512})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.2749073505401611})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.1696934700012207})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.1179521083831787})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.056371808052063})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.0565626621246338})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0746710300445557})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1116979122161865})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6504, 'crossentropy': 1.04632470703125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.3474923372268677})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.1135950088500977})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.069157361984253})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.0131484270095825})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.0222740173339844})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.0116996765136719})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.0182220935821533})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 4935], ['id', 36323], ['id', 15716], ['id', 5374], ['ood', 10319], ['id', 56635], ['id', 48647], ['id', 56627], ['id', 47874], ['id', 59249]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.330389142036438, 0.3255813717842102, 0.3244112730026245, 0.3152766227722168, 0.30891454219818115, 0.3027247190475464, 0.30105745792388916, 0.29986393451690674, 0.2983741760253906, 0.29779261350631714]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.54296875, 'crossentropy': 1.5842599868774414})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.3416169881820679})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.0870060920715332})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.079463005065918})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0308613777160645})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0733505487442017})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0411205291748047})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0954878330230713})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.7085, 'crossentropy': 1.04634658203125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.3363131284713745})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1937904357910156})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0638577938079834})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0781457424163818})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0192524194717407})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0346758365631104})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0337810516357422})
store['active_learning_steps'][37]['eval_training']['best_epoch']=5
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 59091], ['id', 58903], ['id', 31661], ['id', 26219], ['id', 5023], ['id', 7498], ['id', 25486], ['id', 36083], ['id', 5092], ['id', 33781]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.39306095242500305, 0.38745445013046265, 0.3718857765197754, 0.36728113889694214, 0.3628132939338684, 0.3604777753353119, 0.3594959080219269, 0.3594304323196411, 0.3586917519569397, 0.3514809012413025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.486328125, 'crossentropy': 1.5887799263000488})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.2691583633422852})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.186121940612793})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.1228333711624146})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0417217016220093})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0545082092285156})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1254229545593262})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0893630981445312})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6706, 'crossentropy': 1.0543400390625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.53515625, 'crossentropy': 1.298685908317566})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.1148529052734375})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.082749366760254})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.0695202350616455})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.0378293991088867})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.0105516910552979})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.0106016397476196})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 30923], ['id', 16183], ['id', 3830], ['id', 22224], ['id', 12346], ['id', 55475], ['id', 55037], ['id', 59721], ['id', 30098], ['id', 47904]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3594667911529541, 0.33807384967803955, 0.3202555179595947, 0.3188776969909668, 0.31304895877838135, 0.3120368719100952, 0.309794545173645, 0.3092951774597168, 0.30804407596588135, 0.3029071092605591]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.4959324598312378})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.2475194931030273})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.1096645593643188})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1154532432556152})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0644150972366333})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0544226169586182})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.0470788478851318})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0511360168457031})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.066275954246521})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1109015941619873})
store['active_learning_steps'][39]['training']['best_epoch']=7
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6997, 'crossentropy': 1.02551083984375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.3132985830307007})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0928654670715332})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 0.9709869027137756})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0024628639221191})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9766815304756165})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 0.9599117636680603})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 0.9597395062446594})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 0.9790968894958496})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 0.9677180051803589})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 13384], ['id', 1145], ['id', 31216], ['id', 25184], ['id', 51180], ['id', 42887], ['id', 1799], ['id', 52142], ['id', 19484], ['id', 11953]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.32562923431396484, 0.31950247287750244, 0.31462645530700684, 0.31301867961883545, 0.3038524389266968, 0.2950700521469116, 0.29489588737487793, 0.2929123640060425, 0.2850782871246338, 0.2848438024520874]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.5302734375, 'crossentropy': 1.4788439273834229})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.2282934188842773})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1006757020950317})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.037408471107483})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0228769779205322})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.024445652961731})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0186426639556885})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0868315696716309})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9864905476570129})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0109143257141113})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0571818351745605})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.2275660037994385})
store['active_learning_steps'][40]['training']['best_epoch']=9
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.7137, 'crossentropy': 0.994037890625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.4159960746765137})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.179724097251892})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.081342101097107})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 0.9924335479736328})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9372685551643372})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 0.986735463142395})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 0.9258571863174438})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.9701899886131287})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 0.9584623575210571})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 0.9525938630104065})
store['active_learning_steps'][40]['eval_training']['best_epoch']=7
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 52790], ['id', 5135], ['id', 28942], ['id', 17697], ['id', 16608], ['id', 5505], ['id', 13403], ['id', 33779], ['id', 39483], ['id', 49481]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.45032376050949097, 0.4326082468032837, 0.4271920919418335, 0.4059724807739258, 0.40523648262023926, 0.40505504608154297, 0.40418994426727295, 0.4034245014190674, 0.4021183252334595, 0.40155577659606934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.4971649646759033})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.2663977146148682})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1111785173416138})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.031423568725586})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 0.9792172908782959})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 0.9816267490386963})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.052910566329956})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1187230348587036})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6898, 'crossentropy': 0.98878310546875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.369725227355957})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.1087719202041626})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0704888105392456})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0252447128295898})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 0.9701847434043884})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9849156737327576})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 0.9961948394775391})
store['active_learning_steps'][41]['eval_training']['best_epoch']=5
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 54078], ['ood', 1207], ['ood', 33038], ['id', 22069], ['ood', 53028], ['id', 10921], ['id', 22946], ['id', 16361], ['id', 38063], ['id', 58861]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3579261302947998, 0.34285223484039307, 0.3388652801513672, 0.3263368010520935, 0.31861746311187744, 0.31251347064971924, 0.30942296981811523, 0.3083961009979248, 0.3042658567428589, 0.3038429021835327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.5078125, 'crossentropy': 1.543156385421753})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.321340799331665})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1083478927612305})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.0964070558547974})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0090141296386719})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0314874649047852})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0314505100250244})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.051941990852356})
store['active_learning_steps'][42]['training']['best_epoch']=5
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6724, 'crossentropy': 1.03278134765625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.304706335067749})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.1395857334136963})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.0975027084350586})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.0578099489212036})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.018214225769043})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.0026816129684448})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.0422585010528564})
store['active_learning_steps'][42]['eval_training']['best_epoch']=6
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 36843], ['id', 46619], ['id', 31065], ['id', 55016], ['id', 5643], ['id', 43793], ['id', 49135], ['id', 52436], ['id', 37979], ['id', 28940]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.34312307834625244, 0.3293442726135254, 0.3179105520248413, 0.2986499071121216, 0.2921661138534546, 0.29011809825897217, 0.28852927684783936, 0.2857283353805542, 0.2855644226074219, 0.28306710720062256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.501953125, 'crossentropy': 1.5660135746002197})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.252313256263733})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.086944580078125})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.05850088596344})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0009185075759888})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0775465965270996})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.9883448481559753})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0727185010910034})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0658531188964844})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.016709327697754})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.7106, 'crossentropy': 1.01632294921875}
