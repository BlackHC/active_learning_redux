store = {}
store['timestamp']=1622064767
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=1']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=1
store['worker_id']=1
store['num_workers']=80
store['config']={'seed': 1235, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.480844736099243})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.2153875827789307})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.5244293212890625})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.669157028198242})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.5096356868743896})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 4.1095170974731445})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.766690254211426})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5904, 'crossentropy': 4.043133984375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.9198042154312134})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.8559916019439697})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.7087403535842896})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.7164726257324219})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.751434564590454})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.8275588750839233})
store['active_learning_steps'][0]['eval_training']['best_epoch']=6
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 19194], ['ood', 20967], ['ood', 54408], ['id', 13195], ['ood', 54393]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0813960796743767, 1.8488590168054817, 2.443206292812004, 2.874947089932042, 3.114095440144432]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.5805727243423462})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.1948962211608887})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.265253782272339})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.727240562438965})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.52614688873291})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6025, 'crossentropy': 2.2520947265625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.4596002101898193})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.5286288261413574})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.5567784309387207})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.4188423156738281})
store['active_learning_steps'][1]['eval_training']['best_epoch']=4
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 7325], ['id', 7604], ['id', 1807], ['id', 34620], ['id', 6311]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5578738315000884, 1.0578779224237578, 1.475378218304324, 1.806078875773749, 2.0575414884906094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.627345323562622})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.0545785427093506})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.3037636280059814})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.642266273498535})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.701122283935547})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.8487162590026855})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.046001434326172})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.7075085639953613})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.5475950241088867})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.575500965118408})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.9380452632904053})
store['active_learning_steps'][2]['training']['best_epoch']=8
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6045, 'crossentropy': 2.9844458984375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.4505045413970947})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.561560869216919})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.5000979900360107})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.542367935180664})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.621633529663086})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 22576], ['ood', 53026], ['id', 56945], ['id', 54215], ['id', 29729]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7221239404489792, 1.2973498054440853, 1.742525788810311, 2.046490710157207, 2.248121305876129]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.5397639274597168})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.1152641773223877})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.4314780235290527})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.424509048461914})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.7974414825439453})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.00958251953125})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.0218582153320312})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6168, 'crossentropy': 2.6738333984375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.4102246761322021})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.5008554458618164})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.5576753616333008})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.5966041088104248})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.5109405517578125})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.6184349060058594})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 50873], ['id', 53943], ['id', 46439], ['id', 15372], ['id', 37315]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5697106513127956, 1.0915280572661228, 1.5718039785017122, 1.9554736355591427, 2.2071447685522125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.4786455631256104})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.8888776302337646})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.2854373455047607})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.236750602722168})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.734886646270752})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6147, 'crossentropy': 1.950394140625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2981408834457397})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2312171459197998})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2609014511108398})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2720575332641602})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 8506], ['ood', 26255], ['id', 3878], ['ood', 2292], ['id', 33234]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.41030399563174735, 0.7944135408031947, 1.121330209344558, 1.3954682119639843, 1.6312125047564008]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.4634755849838257})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.9675867557525635})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.036886692047119})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.461599588394165})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5045647621154785})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.8451266288757324})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6242, 'crossentropy': 2.064489453125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.4018855094909668})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3583333492279053})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3269517421722412})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3083422183990479})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.307437539100647})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 13354], ['id', 18193], ['id', 13384], ['id', 18865], ['id', 28278]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5648328762948063, 1.0599063545881, 1.4715995198586587, 1.7802360145061682, 2.015310131166645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.3399484157562256})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.6137337684631348})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.83428955078125})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.1091079711914062})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.1320457458496094})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.417994499206543})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6366, 'crossentropy': 1.9810935546875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2388157844543457})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2465136051177979})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2896215915679932})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.319303035736084})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2234927415847778})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 35245], ['id', 36674], ['id', 13464], ['id', 1031], ['id', 23626]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.48769341803741817, 0.9462594224120933, 1.3391213134688558, 1.7030455155712345, 1.984088721454338]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3363702297210693})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.5918865203857422})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.7781405448913574})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.9192593097686768})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.257216691970825})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.3506319522857666})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6504, 'crossentropy': 1.9797798828125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1678107976913452})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2776312828063965})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1727426052093506})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2127487659454346})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1750173568725586})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 5554], ['id', 12883], ['id', 49404], ['id', 46518], ['id', 9921]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6081291549918764, 1.1951629531710366, 1.6118032603391796, 1.9390525042003297, 2.1717563771700403]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.435133934020996})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.4071941375732422})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.84971284866333})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.8680026531219482})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.133704900741577})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.414639711380005})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.3732471466064453})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.452125072479248})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.5419368743896484})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6473, 'crossentropy': 2.29011484375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.3368709087371826})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.5333366394042969})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.5955406427383423})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.5699347257614136})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.4586154222488403})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.4764915704727173})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.563025712966919})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.4187917709350586})
store['active_learning_steps'][8]['eval_training']['best_epoch']=6
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 25738], ['ood', 43683], ['ood', 33697], ['ood', 29664], ['id', 3911]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6540574890305995, 1.1889428778090152, 1.6470931934097512, 1.9940939367845258, 2.280144473360525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.3783296346664429})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.6105592250823975})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.035240411758423})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.1484789848327637})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.2551138401031494})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.5386435985565186})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6112, 'crossentropy': 2.121042578125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2358272075653076})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4246487617492676})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3467479944229126})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2339954376220703})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2786171436309814})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 27763], ['id', 46218], ['id', 31776], ['id', 59615], ['id', 37068]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.58936907423574, 1.116370502996741, 1.5544204420717431, 1.9048317402315034, 2.172211722547699]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.3637468814849854})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.5317623615264893})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.573441505432129})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.8710298538208008})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.761930227279663})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.9954476356506348})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.044732093811035})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.072646141052246})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.5944290161132812})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.334496021270752})
store['active_learning_steps'][10]['training']['best_epoch']=7
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6688, 'crossentropy': 2.1145517578125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.330702781677246})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3461904525756836})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.5005722045898438})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.4847033023834229})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.4096226692199707})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.488213300704956})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.4903819561004639})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.4985688924789429})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.6797055006027222})
store['active_learning_steps'][10]['eval_training']['best_epoch']=6
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 30923], ['id', 28536], ['id', 49841], ['id', 38312], ['ood', 39453]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6362456274679577, 1.1899729023313266, 1.658430447236932, 2.037633541557499, 2.3329360007316575]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.3206474781036377})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.288291335105896})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.6242423057556152})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.5271756649017334})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.8523786067962646})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8422276973724365})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.898057460784912})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6677, 'crossentropy': 1.64211328125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.2710256576538086})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.175234317779541})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1298177242279053})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1419825553894043})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1088740825653076})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1042699813842773})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 1380], ['id', 4461], ['id', 33675], ['id', 59703], ['id', 24287]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5593135720444704, 1.0667639783492517, 1.483811078671435, 1.8308846566214587, 2.096863924077354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3226237297058105})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2797870635986328})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.3192946910858154})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.5653750896453857})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.7414534091949463})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.0224478244781494})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6704, 'crossentropy': 1.4298712890625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.288797378540039})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1609091758728027})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0691123008728027})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0533597469329834})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.06797456741333})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 45727], ['id', 10956], ['id', 18729], ['id', 54405], ['id', 45096]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5672537061074312, 1.0823208463580651, 1.4971475182543479, 1.8007445599147331, 2.023034971303458]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.3763515949249268})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2107868194580078})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3664734363555908})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.4976425170898438})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.657745122909546})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.856109380722046})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.821840763092041})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.9224309921264648})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.9844647645950317})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.1573493480682373})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.1244606971740723})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.0575408935546875})
store['active_learning_steps'][13]['training']['best_epoch']=9
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6736, 'crossentropy': 2.033452734375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.363424301147461})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2311503887176514})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.256365180015564})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2389785051345825})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2223269939422607})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.3051677942276})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2410833835601807})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.321942925453186})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2612488269805908})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2667872905731201})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3070533275604248})
store['active_learning_steps'][13]['eval_training']['best_epoch']=10
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 8628], ['id', 15300], ['id', 24517], ['id', 50385], ['id', 4967]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6830551510259569, 1.2457083146614885, 1.7516599383584919, 2.1860136054374184, 2.5033784730951165]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.4493203163146973})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3534862995147705})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4197185039520264})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.6880967617034912})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.7358622550964355})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.7148076295852661})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.8022408485412598})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6456, 'crossentropy': 1.6882453125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.292251706123352})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.3064773082733154})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.125335931777954})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2151439189910889})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2224879264831543})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.155507206916809})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 56936], ['id', 53873], ['id', 6000], ['id', 57041], ['id', 21144]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.48616395436305737, 0.921781878582109, 1.3012594319422197, 1.6014998020700082, 1.8323604310994916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.3414266109466553})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.218550443649292})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.3658559322357178})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.5649139881134033})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.6100068092346191})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.8283237218856812})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.8261322975158691})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.8162254095077515})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6711, 'crossentropy': 1.6819546875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.3236548900604248})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1580188274383545})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.17397940158844})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1991419792175293})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2200145721435547})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.180070161819458})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 30247], ['id', 1273], ['ood', 33997], ['id', 52331], ['ood', 14265]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5375468278215851, 0.9864610276940553, 1.3835887306744787, 1.7223377539833944, 1.955372072753394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2833205461502075})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1260008811950684})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.3477015495300293})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.3586697578430176})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.4692256450653076})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.6301405429840088})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.6295883655548096})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.5431296825408936})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.7125648260116577})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7873315811157227})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.7260406017303467})
store['active_learning_steps'][16]['training']['best_epoch']=8
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6944, 'crossentropy': 1.6798650390625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.2505340576171875})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0954923629760742})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1041301488876343})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1463234424591064})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1649478673934937})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.065378189086914})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1203869581222534})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1003069877624512})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1051312685012817})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 48763], ['id', 26871], ['id', 50529], ['id', 40742], ['id', 6409]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5716481780016844, 1.082552765637148, 1.5511488726525555, 1.8671818911756954, 2.0915258334563642]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.3135933876037598})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1501985788345337})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.3738689422607422})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.6610097885131836})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.5469167232513428})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.9574742317199707})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.7498562335968018})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.9696040153503418})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6892, 'crossentropy': 1.59414033203125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.256491780281067})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1132290363311768})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0857421159744263})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0936577320098877})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.042895793914795})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.090029001235962})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0693345069885254})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 59611], ['id', 20533], ['id', 246], ['id', 2615], ['id', 59215]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.547379328276105, 1.049352432004314, 1.4277452571328846, 1.7243123002373038, 1.9029612993007694]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.3676652908325195})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1765321493148804})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.25789213180542})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.5049951076507568})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.5002164840698242})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.6245487928390503})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.5959527492523193})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.6322911977767944})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.822131633758545})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7099, 'crossentropy': 1.6448919921875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2616231441497803})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1098828315734863})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0704724788665771})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0492753982543945})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0122582912445068})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0326988697052002})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0015952587127686})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0114619731903076})
store['active_learning_steps'][18]['eval_training']['best_epoch']=7
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 26636], ['id', 57808], ['id', 37572], ['id', 8085], ['id', 52009]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5643558158580433, 1.0931248008789827, 1.5617584590492095, 1.9342374149886092, 2.2064970226865634]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.3363208770751953})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1192855834960938})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2374353408813477})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.283431887626648})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.3743587732315063})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.5022037029266357})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.5824103355407715})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.5995429754257202})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7188, 'crossentropy': 1.411771875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.237452745437622})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0694739818572998})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0206799507141113})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0188546180725098})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.045428991317749})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9792664051055908})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.978950023651123})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 52673], ['id', 18913], ['id', 30561], ['id', 19595], ['id', 25761]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5563768470209043, 1.0085182699926123, 1.403827239729663, 1.7295520935539264, 1.9686447001487029]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.333338737487793})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0655508041381836})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.2105381488800049})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.2275753021240234})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.4446840286254883})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.474541425704956})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.5498270988464355})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7134, 'crossentropy': 1.226376171875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2741488218307495})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0375823974609375})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.0200047492980957})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9931391477584839})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9557853937149048})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9296648502349854})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 49891], ['id', 20054], ['id', 26953], ['id', 12271], ['id', 21731]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.44335746148285904, 0.8497489484908733, 1.2015726297811105, 1.5106078057253765, 1.738874128214162]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2385421991348267})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0828447341918945})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1287879943847656})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.186276912689209})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.320066213607788})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.4692517518997192})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.5236750841140747})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7247, 'crossentropy': 1.173182421875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.3275494575500488})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0221022367477417})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9907757043838501})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9760984182357788})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9729721546173096})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9202755093574524})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 27800], ['id', 52334], ['id', 34750], ['id', 53839], ['id', 55157]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5618137060414008, 1.063308536757904, 1.494982866017752, 1.812568142584361, 2.018279429969297]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.2941348552703857})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.081254482269287})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.029806137084961})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.1631121635437012})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.268406629562378})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.4536316394805908})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.4847521781921387})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.5058271884918213})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.6427257061004639})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.5902111530303955})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.5144741535186768})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.6332037448883057})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.7708115577697754})
store['active_learning_steps'][22]['training']['best_epoch']=10
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7306, 'crossentropy': 1.63397041015625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1684165000915527})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.016990303993225})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0070022344589233})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.044323444366455})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.07741379737854})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.035484790802002})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.0567593574523926})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.0519299507141113})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.0733320713043213})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.0749672651290894})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 1590], ['id', 16530], ['id', 38158], ['id', 47227], ['id', 34122]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6333134992606964, 1.1132568620513812, 1.5407356463205666, 1.8588618266716423, 2.0974340281902073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.4184274673461914})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1330156326293945})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.182349681854248})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.2588615417480469})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.423807144165039})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.426128625869751})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.5750662088394165})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.7166801691055298})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.736236572265625})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.7320020198822021})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.883997917175293})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.9931268692016602})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.0623340606689453})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.7734742164611816})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.967811107635498})
store['active_learning_steps'][23]['training']['best_epoch']=12
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7109, 'crossentropy': 1.984959375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2710964679718018})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0805821418762207})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.067955493927002})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.037714958190918})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1503982543945312})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0608749389648438})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0805678367614746})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0874428749084473})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.076792597770691})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.1000443696975708})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.067887783050537})
store['active_learning_steps'][23]['eval_training']['best_epoch']=8
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 51952], ['id', 10952], ['ood', 18864], ['id', 41561], ['ood', 11984]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6194610165581556, 1.2106101603655004, 1.6899985584351729, 2.0479527940394924, 2.308050975312547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.2957329750061035})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0488982200622559})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1235754489898682})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.1589590311050415})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.2491891384124756})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.3366353511810303})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.4095704555511475})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.421028971672058})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.4248435497283936})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.6831419467926025})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.6765284538269043})
store['active_learning_steps'][24]['training']['best_epoch']=8
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.7362, 'crossentropy': 1.4400775390625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.2277989387512207})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0396778583526611})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0486390590667725})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9931180477142334})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.059899091720581})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0574153661727905})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0308517217636108})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 2462], ['id', 57225], ['id', 58150], ['id', 20011], ['id', 57578]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5442241262410223, 0.9777169313508782, 1.343487489090169, 1.657133013151678, 1.8858732725007874]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.3720018863677979})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0612163543701172})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0745952129364014})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.2643029689788818})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.2875940799713135})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.500683307647705})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.4014098644256592})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.5219790935516357})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.6227118968963623})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.6545956134796143})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.6421411037445068})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.5530284643173218})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.7754297256469727})
store['active_learning_steps'][25]['training']['best_epoch']=10
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7249, 'crossentropy': 1.5867849609375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2739742994308472})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0467954874038696})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.039581537246704})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0472362041473389})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0929838418960571})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.109828233718872})
store['active_learning_steps'][25]['eval_training']['best_epoch']=3
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 17565], ['id', 1610], ['id', 34753], ['id', 7725], ['id', 57386]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6275468689721948, 1.188676662695936, 1.6504845618728554, 2.012171110373095, 2.2624952167861903]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.3539109230041504})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0602190494537354})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1348471641540527})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.1194515228271484})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.2265782356262207})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.3254421949386597})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.3182382583618164})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.4390509128570557})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.5597081184387207})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.5424445867538452})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7246, 'crossentropy': 1.3526787109375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.2687344551086426})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0342772006988525})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.022629976272583})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0002131462097168})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.9597377181053162})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9543306827545166})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.9397402405738831})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9371778964996338})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9447130560874939})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 32583], ['id', 45176], ['id', 55367], ['id', 32930], ['id', 9003]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6525607939376088, 1.1500488577683807, 1.5807682058090027, 1.8979410898711535, 2.1209668454321022]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.3211780786514282})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1491917371749878})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1272118091583252})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.2119619846343994})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.3710837364196777})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.3880109786987305})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.5436935424804688})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.5191826820373535})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.6342605352401733})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.6324577331542969})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.814931869506836})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.6808933019638062})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.7484710216522217})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.7183412313461304})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.9691803455352783})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.8677810430526733})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.003054618835449})
store['active_learning_steps'][27]['training']['best_epoch']=14
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7271, 'crossentropy': 1.744840625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.254319429397583})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0325199365615845})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0738593339920044})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.0663437843322754})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.123387336730957})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.04020094871521})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.1142146587371826})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.1039326190948486})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.1285300254821777})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.0814387798309326})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.055466651916504})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.0374693870544434})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.093897819519043})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.12831711769104})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.128747582435608})
store['active_learning_steps'][27]['eval_training']['best_epoch']=12
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 8065], ['id', 2789], ['id', 31637], ['id', 3908], ['id', 29553]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6559763706943065, 1.1858999666589471, 1.6383009745139105, 1.9939454748680188, 2.240566707938493]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.4174554347991943})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1560447216033936})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0294084548950195})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.1725101470947266})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.2879278659820557})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3059865236282349})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.4498510360717773})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7259, 'crossentropy': 1.151359765625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1648108959197998})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.0292062759399414})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9982199668884277})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.954403817653656})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9563873410224915})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9149676561355591})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 40568], ['id', 47851], ['id', 51163], ['id', 11442], ['id', 31662]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5927317891657231, 1.1027650752548186, 1.5491813533230738, 1.9135177450037268, 2.2090332595325446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2888925075531006})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1061946153640747})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1668524742126465})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.2469536066055298})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3648611307144165})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.4858167171478271})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.256424903869629})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.8041777610778809})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.4379253387451172})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7185, 'crossentropy': 1.42129794921875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2117254734039307})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0315537452697754})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0204925537109375})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9817665815353394})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.984752893447876})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9951049089431763})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9201594591140747})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9700790047645569})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 34402], ['id', 38743], ['id', 29560], ['ood', 54361], ['id', 37194]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5286366736034696, 1.0276580765243541, 1.4735046418951665, 1.8282568867676847, 2.09342423717014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.472775936126709})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2046892642974854})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1196632385253906})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1837477684020996})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.4010777473449707})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.3282911777496338})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.386373519897461})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.2843002080917358})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.434020757675171})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.4162657260894775})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.5891779661178589})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.6190005540847778})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.535994529724121})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.6414681673049927})
store['active_learning_steps'][30]['training']['best_epoch']=11
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7273, 'crossentropy': 1.56920888671875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2070927619934082})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.070975661277771})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0405094623565674})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.002213478088379})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.032480001449585})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0062360763549805})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.0244429111480713})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.0097942352294922})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0189054012298584})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.0125517845153809})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.0014994144439697})
store['active_learning_steps'][30]['eval_training']['best_epoch']=8
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 9033], ['id', 25028], ['id', 47632], ['id', 38271], ['id', 38156]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6659326104284085, 1.212746156257726, 1.6803495056554771, 2.0320627747295177, 2.243275518974535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.325793981552124})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0644984245300293})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0276851654052734})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.1337201595306396})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.1882636547088623})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.3719226121902466})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.452207088470459})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.408554196357727})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.6025893688201904})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.6405410766601562})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.734736442565918})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7307, 'crossentropy': 1.45576494140625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.3439828157424927})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0517547130584717})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0234901905059814})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9925698041915894})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.0181961059570312})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.01140296459198})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0030555725097656})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0188246965408325})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 6714], ['id', 26208], ['id', 269], ['ood', 17602], ['id', 24665]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6161450273215712, 1.1674598446585573, 1.5831086223238433, 1.916808410459061, 2.155303812230298]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.3583065271377563})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.043424367904663})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0911847352981567})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0598816871643066})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.1380436420440674})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.1817526817321777})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.4024511575698853})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.3892614841461182})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.4521479606628418})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.6007426977157593})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.5172109603881836})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7283, 'crossentropy': 1.376722265625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.321260929107666})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0480339527130127})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0071054697036743})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9728823900222778})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.0180681943893433})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9736854434013367})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.0171986818313599})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9974665641784668})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9783423542976379})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9756574630737305})
store['active_learning_steps'][32]['eval_training']['best_epoch']=10
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 50479], ['id', 21165], ['id', 33966], ['ood', 42330], ['id', 13530]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5581769193803101, 1.0630614450412286, 1.5238893634412314, 1.9096023987073583, 2.198716432171561]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.408576250076294})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.164849042892456})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0702855587005615})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0596634149551392})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.1546704769134521})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.2897053956985474})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.2991864681243896})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.3114479780197144})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.3853774070739746})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.5970861911773682})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.6088616847991943})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.6032317876815796})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.6252061128616333})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.5396591424942017})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.7201403379440308})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.637046217918396})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.8419698476791382})
store['active_learning_steps'][33]['training']['best_epoch']=14
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7342, 'crossentropy': 1.59055234375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.307011604309082})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0611817836761475})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.981590747833252})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9934629201889038})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0306923389434814})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0142791271209717})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.0185283422470093})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9842468500137329})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0367460250854492})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9974731206893921})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0200601816177368})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.0064283609390259})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9767870903015137})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0194542407989502})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9780884385108948})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.9760208129882812})
store['active_learning_steps'][33]['eval_training']['best_epoch']=15
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 42917], ['id', 27951], ['id', 18530], ['id', 58841], ['id', 16858]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6967422804854901, 1.3117549771500867, 1.8229544928760202, 2.1821293714549226, 2.402705376476936]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3284049034118652})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0507646799087524})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.042333960533142})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.1024997234344482})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.0478768348693848})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.1472442150115967})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.3144655227661133})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.3685420751571655})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.5050647258758545})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7315, 'crossentropy': 1.189611328125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.388741374015808})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.058791995048523})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9815891981124878})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 0.9510430097579956})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9193849563598633})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.9685640335083008})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9082667827606201})
store['active_learning_steps'][34]['eval_training']['best_epoch']=4
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 17500], ['id', 49864], ['id', 46216], ['id', 33694], ['id', 14314]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5215646017913513, 1.0009759315429103, 1.4006392225551867, 1.7032931983714983, 1.9260565047994378]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 1.4041047096252441})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0656986236572266})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9991491436958313})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.0147411823272705})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.076353669166565})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.1709355115890503})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.240706205368042})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.297253966331482})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.3172069787979126})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.4591865539550781})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.5137832164764404})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.516623616218567})
store['active_learning_steps'][35]['training']['best_epoch']=9
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7354, 'crossentropy': 1.32394462890625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.5625, 'crossentropy': 1.3663215637207031})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.074155569076538})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.025791883468628})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9514940977096558})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.9605961441993713})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9694594144821167})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.9504090547561646})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9499409794807434})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.9320721626281738})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 0.9253228902816772})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9493892788887024})
store['active_learning_steps'][35]['eval_training']['best_epoch']=10
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 20650], ['id', 36323], ['id', 34238], ['id', 43374], ['id', 45010]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5511947375108952, 1.0655936340148746, 1.476081360145649, 1.8111754863472642, 2.0615448937216865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.3089025020599365})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.041395902633667})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.0009251832962036})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.1559298038482666})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.1924021244049072})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.2205066680908203})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.4534764289855957})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.5171451568603516})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.478400468826294})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7274, 'crossentropy': 1.23926416015625}
