store = {}
store['timestamp']=1620259978
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=26']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=26
store['worker_id']=26
store['num_workers']=40
store['config']={'seed': 32, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.343252182006836})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.401820659637451})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.957216739654541})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.773019313812256})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6847, 'crossentropy': 2.037783984375}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 2953], ['ood', 5147], ['id', 14249], ['id', 44118], ['ood', 53261]], 'labels': [6, 6, 9, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.6646056175231934})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.9649401903152466})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.135540008544922})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.1467795372009277})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6829, 'crossentropy': 1.545129296875}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 41175], ['ood', 32452], ['id', 52336], ['id', 39911], ['id', 14193]], 'labels': [8, 7, 0, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.537970781326294})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.769918441772461})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.7752974033355713})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.8263039588928223})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6978, 'crossentropy': 1.40587060546875}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 8380], ['ood', 18320], ['id', 10437], ['ood', 53235], ['id', 46815]], 'labels': [4, 7, 4, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.311697244644165})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.327071189880371})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.443786382675171})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.4785139560699463})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7348, 'crossentropy': 1.1803890625}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 44867], ['id', 28726], ['id', 14317], ['ood', 59537], ['ood', 14600]], 'labels': [0, 8, 9, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.4321787357330322})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.4901156425476074})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.5825552940368652})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.668816089630127})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6801, 'crossentropy': 1.381209765625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 18420], ['id', 50700], ['id', 57419], ['ood', 278], ['id', 34310]], 'labels': [4, 2, 6, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.2457354068756104})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.295423150062561})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.5665637254714966})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.6693952083587646})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7183, 'crossentropy': 1.20976474609375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 36239], ['ood', 37772], ['id', 8744], ['ood', 28858], ['id', 8363]], 'labels': [1, 6, 5, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4094526767730713})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.6886563301086426})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.896878719329834})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.1145596504211426})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6795, 'crossentropy': 1.28804677734375}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 23640], ['ood', 22282], ['ood', 26537], ['id', 56212], ['id', 29330]], 'labels': [5, 3, 1, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.2352832555770874})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.2874947786331177})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.3943383693695068})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.4746603965759277})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7323, 'crossentropy': 1.11307265625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 54505], ['ood', 41585], ['ood', 19210], ['id', 37609], ['id', 41399]], 'labels': [8, 7, 2, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.2045972347259521})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.2385797500610352})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.5582419633865356})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.6109169721603394})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7424, 'crossentropy': 1.1450361328125}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 38446], ['id', 5923], ['id', 33219], ['ood', 59311], ['id', 1779]], 'labels': [0, 3, 0, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.1507549285888672})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.2705423831939697})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.398256778717041})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.5172276496887207})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7503, 'crossentropy': 1.079778515625}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 49757], ['ood', 41238], ['id', 23713], ['id', 49828], ['id', 27878]], 'labels': [1, 1, 4, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.10226571559906})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.107574701309204})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.291269063949585})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.4514734745025635})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7505, 'crossentropy': 1.10353388671875}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 28396], ['id', 59674], ['ood', 397], ['ood', 8253], ['ood', 16340]], 'labels': [6, 4, 4, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.1067712306976318})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0735751390457153})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.2400779724121094})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.328711748123169})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.3970770835876465})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7979, 'crossentropy': 0.99634970703125}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 2422], ['ood', 58727], ['ood', 51364], ['id', 21177], ['ood', 2536]], 'labels': [5, 3, 5, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.0386826992034912})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.00132417678833})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0944397449493408})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.1168696880340576})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0470850467681885})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8136, 'crossentropy': 0.89680380859375}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 28052], ['ood', 50158], ['ood', 7736], ['id', 10995], ['id', 12531]], 'labels': [3, 0, 5, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.1306090354919434})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.1486914157867432})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.1873570680618286})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.2833352088928223})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.768, 'crossentropy': 1.0413044921875}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 11679], ['ood', 58473], ['ood', 26545], ['ood', 18951], ['ood', 37289]], 'labels': [9, 7, 3, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.1368895769119263})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.1582282781600952})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.2547483444213867})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.4812359809875488})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7717, 'crossentropy': 1.04235283203125}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 50811], ['id', 20356], ['id', 26869], ['ood', 50875], ['ood', 33142]], 'labels': [0, 3, 4, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.32216215133667})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.2979265451431274})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.4287099838256836})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.6242403984069824})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.5625629425048828})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7703, 'crossentropy': 1.14858740234375}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 40453], ['id', 57792], ['ood', 59711], ['id', 323], ['ood', 22210]], 'labels': [1, 7, 2, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.9632941484451294})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9418649673461914})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0631049871444702})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.2389941215515137})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.1535980701446533})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8249, 'crossentropy': 0.90274482421875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 28241], ['id', 54520], ['id', 46426], ['id', 43005], ['ood', 33539]], 'labels': [8, 9, 7, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8891253471374512})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8507524728775024})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0175704956054688})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0182576179504395})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0700361728668213})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8479, 'crossentropy': 0.808692138671875}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 34846], ['id', 496], ['ood', 46473], ['id', 13469], ['ood', 23364]], 'labels': [6, 5, 1, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9051752090454102})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9062232375144958})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9373800754547119})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9561756253242493})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8274, 'crossentropy': 0.8813625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 39053], ['id', 32607], ['ood', 18446], ['ood', 32505], ['id', 53278]], 'labels': [7, 8, 5, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.9933632612228394})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9395080804824829})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.029571294784546})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1462632417678833})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0910011529922485})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8258, 'crossentropy': 0.86297900390625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 51886], ['ood', 23290], ['id', 24188], ['id', 40873], ['ood', 2951]], 'labels': [5, 0, 0, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9741537570953369})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9497494697570801})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9791271686553955})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1915488243103027})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1517231464385986})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8306, 'crossentropy': 0.83842841796875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 43110], ['ood', 24209], ['id', 49881], ['id', 19676], ['ood', 42552]], 'labels': [8, 7, 4, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 0.965164065361023})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8464038372039795})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9270104169845581})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0405219793319702})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0297529697418213})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8358, 'crossentropy': 0.789813037109375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 52857], ['id', 23832], ['ood', 10802], ['id', 40490], ['id', 19312]], 'labels': [5, 5, 7, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0290604829788208})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.885124921798706})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0649421215057373})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.226878046989441})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1768808364868164})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8227, 'crossentropy': 0.854787890625}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 6065], ['id', 9539], ['id', 48482], ['id', 24244], ['id', 15382]], 'labels': [8, 5, 3, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.843017041683197})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9258476495742798})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8751555681228638})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8477725386619568})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8368, 'crossentropy': 0.7914701171875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 12340], ['ood', 14788], ['id', 3607], ['id', 5528], ['id', 46996]], 'labels': [6, 2, 2, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9232958555221558})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7568525075912476})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8567001819610596})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9343597888946533})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8510319590568542})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8461, 'crossentropy': 0.744279296875}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 15075], ['id', 38555], ['ood', 57959], ['ood', 45604], ['id', 43930]], 'labels': [2, 6, 5, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9669793248176575})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8745511770248413})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9476219415664673})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9412678480148315})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9718360900878906})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8418, 'crossentropy': 0.79885234375}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 47540], ['id', 7364], ['id', 3057], ['id', 2520], ['id', 2327]], 'labels': [9, 0, 3, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9297429323196411})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8115047216415405})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9923860430717468})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0454740524291992})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0524709224700928})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8521, 'crossentropy': 0.74376748046875}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 15713], ['ood', 9012], ['ood', 50668], ['ood', 1587], ['ood', 24195]], 'labels': [2, 7, 4, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8508338928222656})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.7898913621902466})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7833592891693115})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9544916749000549})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0002607107162476})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9745476245880127})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8602, 'crossentropy': 0.713624462890625}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 25140], ['ood', 5343], ['id', 54793], ['ood', 41075], ['id', 51612]], 'labels': [0, 7, 9, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9606364965438843})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8294006586074829})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9419949650764465})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0337371826171875})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0486245155334473})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8525, 'crossentropy': 0.77987333984375}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 42329], ['id', 11154], ['id', 1834], ['ood', 10626], ['ood', 48273]], 'labels': [1, 5, 5, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9544610977172852})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8399598598480225})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.888624906539917})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9456840753555298})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.080831527709961})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8351, 'crossentropy': 0.76848583984375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 22799], ['ood', 53696], ['id', 57070], ['ood', 47968], ['id', 30299]], 'labels': [9, 2, 8, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0775644779205322})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9860512018203735})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8832486867904663})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0249799489974976})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0367166996002197})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0798237323760986})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8391, 'crossentropy': 0.830403515625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 31057], ['ood', 49278], ['ood', 16064], ['id', 39381], ['id', 3524]], 'labels': [9, 7, 3, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9452711939811707})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.830274224281311})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9050196409225464})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9710962176322937})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9356217980384827})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8514, 'crossentropy': 0.720020849609375}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 4297], ['ood', 5935], ['ood', 13030], ['id', 41634], ['id', 38019]], 'labels': [5, 4, 7, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9735411405563354})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8689688444137573})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8804035782814026})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9518158435821533})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.036075234413147})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8312, 'crossentropy': 0.79945087890625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 2865], ['ood', 44128], ['id', 12308], ['ood', 38737], ['ood', 7646]], 'labels': [7, 7, 8, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9818229675292969})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.888748824596405})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9404551982879639})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9837484359741211})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.071512222290039})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8338, 'crossentropy': 0.8039541015625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 21994], ['id', 41662], ['ood', 50675], ['ood', 21695], ['ood', 28652]], 'labels': [4, 2, 4, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9703745245933533})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8133330345153809})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.840587854385376})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9107542634010315})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.989378809928894})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8378, 'crossentropy': 0.783261376953125}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 2286], ['ood', 19507], ['ood', 42420], ['id', 20420], ['id', 45418]], 'labels': [3, 5, 3, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9421758651733398})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.7922942638397217})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8470497131347656})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.836711049079895})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8516707420349121})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8434, 'crossentropy': 0.719900537109375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 40820], ['id', 57507], ['id', 27921], ['id', 35477], ['ood', 9591]], 'labels': [0, 0, 5, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9523905515670776})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8044555187225342})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8072992563247681})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7837768793106079})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9284660220146179})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.963365912437439})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9790562391281128})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8646, 'crossentropy': 0.72894130859375}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 22872], ['id', 47588], ['id', 21234], ['ood', 23125], ['ood', 42448]], 'labels': [6, 9, 6, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8925817012786865})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.771287202835083})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8152538537979126})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8108245134353638})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9585219621658325})
store['active_learning_steps'][37]['training']['best_epoch']=2
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8526, 'crossentropy': 0.7065375}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 15146], ['id', 7288], ['ood', 34266], ['ood', 18417], ['ood', 15782]], 'labels': [9, 3, 1, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9273236989974976})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8414901494979858})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8165144920349121})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9907201528549194})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9118101596832275})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9983134865760803})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8587, 'crossentropy': 0.744100634765625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 24676], ['ood', 16370], ['id', 18243], ['ood', 22805], ['id', 56828]], 'labels': [0, 4, 3, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.860956072807312})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7643382549285889})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7762091159820557})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7821093797683716})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8642847537994385})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8626, 'crossentropy': 0.67915302734375}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 41754], ['ood', 43585], ['id', 43805], ['id', 23005], ['ood', 50229]], 'labels': [5, 1, 5, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9029579162597656})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7424551248550415})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7371349334716797})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8596030473709106})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.857383131980896})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9901082515716553})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8762, 'crossentropy': 0.655913525390625}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 55953], ['ood', 18258], ['ood', 10832], ['ood', 7544], ['ood', 9749]], 'labels': [8, 5, 8, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8797931671142578})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7333360910415649})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7819206714630127})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7660375833511353})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8329348564147949})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8579, 'crossentropy': 0.6827486328125}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 57910], ['id', 55295], ['id', 50953], ['ood', 15318], ['ood', 50608]], 'labels': [2, 9, 2, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8674331903457642})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.703454852104187})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.777640700340271})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7378271818161011})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8469723463058472})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8706, 'crossentropy': 0.651868701171875}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 27503], ['id', 51313], ['id', 29601], ['ood', 34364], ['id', 30596]], 'labels': [6, 8, 8, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9060369729995728})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7064152956008911})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7252848744392395})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7405192852020264})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6811913251876831})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7961228489875793})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6959328651428223})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8455663919448853})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8909, 'crossentropy': 0.6521521484375}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 15464], ['id', 45189], ['id', 8408], ['id', 2832], ['ood', 14709]], 'labels': [1, 0, 9, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8550879955291748})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7447748184204102})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7566474676132202})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7394292950630188})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8374688625335693})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8131096959114075})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7771101593971252})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.875, 'crossentropy': 0.672123779296875}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 4698], ['id', 55310], ['ood', 8448], ['ood', 40105], ['ood', 43677]], 'labels': [8, 1, 4, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8324334025382996})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.80759596824646})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7633734941482544})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7569998502731323})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.832626223564148})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7832401394844055})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8583694696426392})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8789, 'crossentropy': 0.684937841796875}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 32138], ['ood', 56812], ['ood', 41189], ['ood', 2743], ['ood', 17849]], 'labels': [1, 0, 6, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9234358668327332})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6670422554016113})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7768915295600891})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8432019948959351})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8973183035850525})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8797, 'crossentropy': 0.626917578125}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 39003], ['id', 11661], ['id', 16609], ['id', 44609], ['ood', 29671]], 'labels': [7, 0, 7, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9269475936889648})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7299042344093323})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7221956253051758})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.77081698179245})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.866460919380188})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8233639001846313})
store['active_learning_steps'][47]['training']['best_epoch']=3
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.877, 'crossentropy': 0.672208984375}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 55421], ['ood', 17173], ['ood', 37794], ['id', 25029], ['ood', 19185]], 'labels': [3, 9, 3, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9268957376480103})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7721636891365051})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7855494022369385})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7813715934753418})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8748809099197388})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.858, 'crossentropy': 0.7077095703125}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 12637], ['ood', 97], ['id', 7875], ['id', 53498], ['id', 5081]], 'labels': [5, 1, 0, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8837461471557617})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7212800979614258})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7607854604721069})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7467566132545471})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7663134336471558})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8559, 'crossentropy': 0.675845556640625}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 33020], ['id', 42205], ['ood', 10742], ['ood', 48312], ['id', 53186]], 'labels': [2, 1, 8, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.943458616733551})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7028869390487671})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7397892475128174})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7855435013771057})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7666783332824707})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.876, 'crossentropy': 0.63638076171875}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 5819], ['id', 53931], ['id', 35817], ['ood', 2599], ['ood', 12687]], 'labels': [8, 7, 6, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8941652774810791})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7195959091186523})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7346360087394714})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7179304361343384})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7467231750488281})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.820982813835144})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7556963562965393})
store['active_learning_steps'][51]['training']['best_epoch']=4
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8868, 'crossentropy': 0.6236408203125}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 22863], ['id', 6552], ['ood', 28097], ['id', 38394], ['ood', 2130]], 'labels': [3, 4, 1, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9071666598320007})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.734491765499115})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7074853181838989})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7158240079879761})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6826558113098145})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8486805558204651})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8728351593017578})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8098087310791016})
store['active_learning_steps'][52]['training']['best_epoch']=5
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8898, 'crossentropy': 0.635495751953125}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 56170], ['ood', 36728], ['id', 14148], ['id', 53676], ['id', 16215]], 'labels': [8, 2, 0, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8882126808166504})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7798608541488647})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7026498317718506})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7915027141571045})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.849055290222168})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7664262056350708})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8861, 'crossentropy': 0.61454423828125}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 57724], ['ood', 42798], ['ood', 54656], ['id', 4339], ['ood', 20908]], 'labels': [4, 7, 9, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8778202533721924})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6537201404571533})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6532670259475708})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7273008227348328})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.764660120010376})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7491376399993896})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.89, 'crossentropy': 0.59280556640625}
store['active_learning_steps'][54]['acquisition']={'indices': [['id', 13974], ['id', 46027], ['id', 33295], ['ood', 49995], ['ood', 6528]], 'labels': [1, 3, 1, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9257159233093262})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6551313400268555})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6799100637435913})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6907926797866821})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.751244306564331})
store['active_learning_steps'][55]['training']['best_epoch']=2
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8815, 'crossentropy': 0.612879150390625}
store['active_learning_steps'][55]['acquisition']={'indices': [['ood', 1887], ['id', 33480], ['id', 43455], ['ood', 45666], ['ood', 20873]], 'labels': [5, 1, 8, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8182935118675232})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.656752347946167})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6830226182937622})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6489723920822144})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7152119874954224})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7551224231719971})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7067225575447083})
store['active_learning_steps'][56]['training']['best_epoch']=4
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8963, 'crossentropy': 0.5797787109375}
store['active_learning_steps'][56]['acquisition']={'indices': [['ood', 59142], ['ood', 40064], ['id', 53488], ['id', 34618], ['id', 30831]], 'labels': [2, 8, 3, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8537360429763794})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6777180433273315})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5959112048149109})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6980826258659363})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7596831321716309})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7343503832817078})
store['active_learning_steps'][57]['training']['best_epoch']=3
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.899, 'crossentropy': 0.55018974609375}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 28295], ['ood', 15306], ['ood', 26435], ['id', 46311], ['id', 46375]], 'labels': [8, 0, 9, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8484489917755127})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6476881504058838})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6476060152053833})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7311298251152039})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7582422494888306})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7805266380310059})
store['active_learning_steps'][58]['training']['best_epoch']=3
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8968, 'crossentropy': 0.56301181640625}
store['active_learning_steps'][58]['acquisition']={'indices': [['ood', 8147], ['ood', 28704], ['ood', 27889], ['ood', 55402], ['id', 44466]], 'labels': [8, 9, 2, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8527480363845825})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7271970510482788})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6590522527694702})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7292495965957642})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.770620584487915})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6589705944061279})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7449407577514648})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7616565227508545})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7526405453681946})
store['active_learning_steps'][59]['training']['best_epoch']=6
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.6113697265625}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 34787], ['id', 35634], ['ood', 11398], ['ood', 9781], ['ood', 35931]], 'labels': [8, 0, 7, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9519784450531006})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6929577589035034})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.652062177658081})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.637169599533081})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6253411769866943})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7051346302032471})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7390331029891968})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.786713719367981})
store['active_learning_steps'][60]['training']['best_epoch']=5
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9068, 'crossentropy': 0.576895263671875}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 2145], ['ood', 55716], ['id', 50829], ['ood', 11303], ['ood', 40370]], 'labels': [7, 9, 1, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8388440608978271})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6880649924278259})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6515974998474121})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6803778409957886})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7225451469421387})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6959222555160522})
store['active_learning_steps'][61]['training']['best_epoch']=3
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8972, 'crossentropy': 0.553842578125}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 37196], ['id', 42503], ['ood', 51262], ['ood', 38250], ['ood', 39581]], 'labels': [1, 2, 2, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8623537421226501})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7233405113220215})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.705091118812561})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6801512241363525})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7109665274620056})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.689461350440979})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6991798877716064})
store['active_learning_steps'][62]['training']['best_epoch']=4
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8965, 'crossentropy': 0.596562060546875}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 45947], ['id', 44150], ['ood', 4581], ['id', 42287], ['id', 14871]], 'labels': [5, 7, 0, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8410253524780273})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6346604824066162})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6708341836929321})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6415853500366211})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6095645427703857})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6751289963722229})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7366849184036255})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7236019372940063})
store['active_learning_steps'][63]['training']['best_epoch']=5
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9096, 'crossentropy': 0.52746796875}
store['active_learning_steps'][63]['acquisition']={'indices': [['ood', 53149], ['id', 56544], ['id', 17658], ['ood', 13307], ['id', 44204]], 'labels': [5, 8, 8, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8584957122802734})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6756690144538879})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6066818237304688})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6387455463409424})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6298279762268066})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6057847738265991})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7032037377357483})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6878695487976074})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7158735990524292})
store['active_learning_steps'][64]['training']['best_epoch']=6
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9121, 'crossentropy': 0.543521484375}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 43490], ['id', 35879], ['ood', 52912], ['ood', 26132], ['ood', 3163]], 'labels': [1, 4, 9, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8516908288002014})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6595643758773804})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6594376564025879})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6729497909545898})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7105309963226318})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6818358898162842})
store['active_learning_steps'][65]['training']['best_epoch']=3
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8976, 'crossentropy': 0.550677734375}
store['active_learning_steps'][65]['acquisition']={'indices': [['ood', 4850], ['id', 13430], ['ood', 36669], ['id', 42380], ['ood', 37795]], 'labels': [1, 4, 2, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8505153656005859})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6833277940750122})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6182564496994019})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6189320087432861})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6896659135818481})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6169788837432861})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.707893967628479})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7143538594245911})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6926751136779785})
store['active_learning_steps'][66]['training']['best_epoch']=6
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9168, 'crossentropy': 0.513453515625}
store['active_learning_steps'][66]['acquisition']={'indices': [['ood', 51170], ['ood', 7413], ['ood', 52298], ['ood', 2909], ['id', 188]], 'labels': [9, 3, 6, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8750603199005127})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6979550123214722})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6808109879493713})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6998342275619507})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6667461395263672})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6681286096572876})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7196100950241089})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7083268165588379})
store['active_learning_steps'][67]['training']['best_epoch']=5
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9001, 'crossentropy': 0.581693896484375}
store['active_learning_steps'][67]['acquisition']={'indices': [['ood', 16216], ['ood', 44411], ['ood', 1472], ['id', 35479], ['ood', 25652]], 'labels': [2, 2, 6, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8566352128982544})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6548696756362915})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7001060247421265})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.690308690071106})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6548449993133545})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.697659432888031})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7237644195556641})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7023580074310303})
store['active_learning_steps'][68]['training']['best_epoch']=5
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9122, 'crossentropy': 0.54113701171875}
store['active_learning_steps'][68]['acquisition']={'indices': [['ood', 48080], ['id', 18647], ['id', 39835], ['id', 3452], ['id', 47807]], 'labels': [3, 1, 7, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8674041032791138})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6778209209442139})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6406270861625671})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5888737440109253})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6310528516769409})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6747058629989624})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.623917818069458})
store['active_learning_steps'][69]['training']['best_epoch']=4
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9089, 'crossentropy': 0.52216005859375}
store['active_learning_steps'][69]['acquisition']={'indices': [['ood', 13938], ['id', 11066], ['id', 35113], ['ood', 1236], ['id', 45571]], 'labels': [8, 2, 3, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8355839252471924})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6774620413780212})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6785234212875366})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6549709439277649})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6543388366699219})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7167226076126099})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.74881911277771})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6576606035232544})
store['active_learning_steps'][70]['training']['best_epoch']=5
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8994, 'crossentropy': 0.616938818359375}
store['active_learning_steps'][70]['acquisition']={'indices': [['ood', 56530], ['id', 7257], ['ood', 27225], ['id', 28774], ['ood', 3441]], 'labels': [8, 2, 4, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9228994846343994})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6669526100158691})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6203916072845459})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6685488224029541})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6417151093482971})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7304865717887878})
store['active_learning_steps'][71]['training']['best_epoch']=3
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9048, 'crossentropy': 0.53362978515625}
store['active_learning_steps'][71]['acquisition']={'indices': [['ood', 14521], ['ood', 58924], ['ood', 57593], ['ood', 26818], ['id', 35441]], 'labels': [6, 3, 4, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8356093168258667})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6476151943206787})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6245653629302979})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6351313591003418})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6286384463310242})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6619375944137573})
store['active_learning_steps'][72]['training']['best_epoch']=3
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8926, 'crossentropy': 0.572014111328125}
store['active_learning_steps'][72]['acquisition']={'indices': [['ood', 9226], ['id', 41237], ['id', 55229], ['ood', 51227], ['id', 770]], 'labels': [2, 1, 5, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8247325420379639})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6463439464569092})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.645922064781189})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6377681493759155})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6927253603935242})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7149767875671387})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7056193351745605})
store['active_learning_steps'][73]['training']['best_epoch']=4
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9031, 'crossentropy': 0.539244970703125}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 55868], ['ood', 7588], ['id', 37129], ['ood', 32541], ['id', 41131]], 'labels': [8, 3, 8, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7745414972305298})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6220229864120483})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6115765571594238})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6235185861587524})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6570366621017456})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.660401463508606})
store['active_learning_steps'][74]['training']['best_epoch']=3
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9018, 'crossentropy': 0.5250716796875}
store['active_learning_steps'][74]['acquisition']={'indices': [['ood', 42721], ['ood', 33577], ['id', 43200], ['ood', 45885], ['id', 41525]], 'labels': [7, 7, 3, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.88286292552948})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6229516267776489})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6328734159469604})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6676070094108582})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6249101161956787})
store['active_learning_steps'][75]['training']['best_epoch']=2
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.8893, 'crossentropy': 0.58386318359375}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 17865], ['ood', 4080], ['id', 19438], ['id', 35676], ['id', 34957]], 'labels': [7, 1, 3, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8567341566085815})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6220482587814331})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5979669094085693})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.599567711353302})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6333720684051514})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6519622802734375})
store['active_learning_steps'][76]['training']['best_epoch']=3
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9019, 'crossentropy': 0.527585595703125}
store['active_learning_steps'][76]['acquisition']={'indices': [['ood', 50321], ['id', 28684], ['id', 13985], ['id', 46617], ['ood', 33104]], 'labels': [9, 2, 1, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8952416181564331})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.60915207862854})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6373246908187866})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6360499858856201})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6428098678588867})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.8914, 'crossentropy': 0.574828515625}
store['active_learning_steps'][77]['acquisition']={'indices': [['ood', 4610], ['ood', 36679], ['ood', 12609], ['id', 4842], ['id', 36887]], 'labels': [2, 6, 1, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8968514204025269})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6278671026229858})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.639428436756134})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6290417909622192})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6076645851135254})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6123645305633545})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6730430126190186})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.668698787689209})
store['active_learning_steps'][78]['training']['best_epoch']=5
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.909, 'crossentropy': 0.52448798828125}
store['active_learning_steps'][78]['acquisition']={'indices': [['ood', 56781], ['id', 44939], ['ood', 43742], ['ood', 45548], ['id', 6726]], 'labels': [5, 5, 1, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9055904150009155})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6873324513435364})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6113685369491577})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6172673106193542})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6104567050933838})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6482727527618408})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6956439018249512})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7139736413955688})
store['active_learning_steps'][79]['training']['best_epoch']=5
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9083, 'crossentropy': 0.540835791015625}
store['active_learning_steps'][79]['acquisition']={'indices': [['ood', 49171], ['ood', 41830], ['ood', 50501], ['ood', 49721], ['id', 21367]], 'labels': [8, 9, 3, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8140626549720764})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.61214280128479})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5890798568725586})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6234616041183472})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6415702104568481})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6661848425865173})
store['active_learning_steps'][80]['training']['best_epoch']=3
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9044, 'crossentropy': 0.504582177734375}
store['active_learning_steps'][80]['acquisition']={'indices': [['ood', 56025], ['ood', 23975], ['id', 28680], ['id', 43187], ['id', 55025]], 'labels': [2, 7, 6, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8544365167617798})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7012423872947693})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5866005420684814})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5525115728378296})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.559964656829834})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5968369841575623})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6250383853912354})
store['active_learning_steps'][81]['training']['best_epoch']=4
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.4793650390625}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 56717], ['ood', 18829], ['ood', 49755], ['id', 28956], ['ood', 20585]], 'labels': [1, 3, 9, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8485657572746277})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6196436285972595})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6077630519866943})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5936102867126465})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6041324138641357})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6300559043884277})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6601239442825317})
store['active_learning_steps'][82]['training']['best_epoch']=4
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9089, 'crossentropy': 0.517585009765625}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 21172], ['id', 15694], ['ood', 7514], ['id', 56050], ['ood', 4739]], 'labels': [9, 0, 6, 0, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8930072784423828})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6913940906524658})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.639378011226654})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6496137380599976})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6507241725921631})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6728945970535278})
store['active_learning_steps'][83]['training']['best_epoch']=3
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9064, 'crossentropy': 0.541906201171875}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 34685], ['id', 37484], ['id', 39628], ['ood', 747], ['id', 16855]], 'labels': [3, 2, 0, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.850786566734314})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.660713255405426})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.634565532207489})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6481645107269287})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5999288558959961})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6035288572311401})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6465556621551514})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6668474078178406})
store['active_learning_steps'][84]['training']['best_epoch']=5
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.52218974609375}
store['active_learning_steps'][84]['acquisition']={'indices': [['ood', 22122], ['id', 16258], ['ood', 59980], ['id', 46214], ['id', 19640]], 'labels': [4, 6, 3, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7981669902801514})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6243903040885925})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6317762136459351})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6326671242713928})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6252445578575134})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.891, 'crossentropy': 0.560622021484375}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 45489], ['id', 1227], ['ood', 56685], ['ood', 51140], ['ood', 7850]], 'labels': [7, 4, 3, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9229604005813599})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6202830076217651})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5930303335189819})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6160427331924438})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6067287921905518})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5931330919265747})
store['active_learning_steps'][86]['training']['best_epoch']=3
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.49104326171875}
