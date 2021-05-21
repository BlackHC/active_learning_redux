store = {}
store['timestamp']=1621482225
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=72']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=72
store['worker_id']=72
store['num_workers']=80
store['config']={'seed': 1310, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.2475297451019287})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.544626235961914})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.6148180961608887})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.7572786808013916})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.672, 'crossentropy': 2.064549609375}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 11661], ['id', 26013], ['id', 57632], ['id', 55311], ['id', 8810]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2203316070472574, 2.2481241110830146, 3.0460618664929715, 3.6142517444330977, 3.982303623497887]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.0045166015625})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.477281093597412})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.611384868621826})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 3.0414724349975586})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.7319822311401367})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.815176486968994})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7123, 'crossentropy': 2.396160546875}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 7674], ['id', 12342], ['id', 56061], ['id', 33804], ['id', 39679]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.3015838694876263, 2.4039739935830227, 3.2709217130165182, 3.8413476309507466, 4.168956246940431]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.716078519821167})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.9556543827056885})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.3431432247161865})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.4752066135406494})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.417975425720215})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7419, 'crossentropy': 1.7803408203125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 12127], ['id', 3205], ['id', 51544], ['id', 54461], ['id', 8886]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1585317358708709, 2.1579390341551434, 2.989309349904479, 3.584372347895142, 3.9867829755858057]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.8285918235778809})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.2568936347961426})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.39139986038208})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.3506948947906494})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.3190362453460693})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.8313331604003906})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.7499356269836426})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.3361334800720215})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7348, 'crossentropy': 2.211126953125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 32348], ['id', 15893], ['id', 17057], ['id', 25039], ['id', 36197]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.2987743072630007, 2.3876995749089143, 3.2164755598868924, 3.7992438105432527, 4.143515664291325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.5469657182693481})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.6651132106781006})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.7576801776885986})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.867230772972107})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.1602067947387695})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 2.1045117378234863})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.9052661657333374})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.8586686849594116})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 2.0904650688171387})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.4853358268737793})
store['active_learning_steps'][4]['training']['best_epoch']=7
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7917, 'crossentropy': 1.689669921875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 26519], ['id', 42799], ['id', 26511], ['id', 23946], ['id', 6582]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.2642837123133126, 2.384530629150181, 3.2206080272748663, 3.793404698493849, 4.159552477637507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.4193100929260254})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.9402364492416382})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.8145873546600342})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.8785169124603271})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 2.0052688121795654})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.7255502939224243})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.156619071960449})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7807, 'crossentropy': 1.6214458984375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 4767], ['id', 10298], ['id', 46530], ['id', 12950], ['id', 40422]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.206542819239103, 2.265557932787227, 3.1288127027580037, 3.766785007103259, 4.136910912726634]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.334526538848877})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.388950228691101})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.470266342163086})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.6007496118545532})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.8269765377044678})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.5730243921279907})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.9521539211273193})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7943, 'crossentropy': 1.41592685546875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 24038], ['id', 29591], ['id', 38553], ['id', 19855], ['id', 31761]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1614996487995433, 2.2565983294933067, 3.0954528767253064, 3.6963796836442313, 4.0751156699025834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.2728760242462158})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.6758675575256348})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.6645548343658447})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.6891982555389404})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.8739745616912842})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.7362008094787598})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 2.096370220184326})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.9207286834716797})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8005, 'crossentropy': 1.54198515625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 15848], ['id', 47260], ['id', 37048], ['id', 15987], ['id', 28390]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.199450606790794, 2.258363472104839, 3.1287538714909946, 3.7491359767255785, 4.127778044019825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.3062410354614258})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.5198640823364258})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.643485188484192})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.5104963779449463})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.8135044574737549})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.9522662162780762})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.5796705484390259})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.847882866859436})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.856874942779541})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 2.067877769470215})
store['active_learning_steps'][8]['training']['best_epoch']=7
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7901, 'crossentropy': 1.40529921875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 14329], ['id', 34318], ['id', 47132], ['id', 20436], ['id', 49088]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.1507365781360237, 2.2084563437424265, 3.08311143349723, 3.690029936630731, 4.0805787302207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.257541298866272})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.2397713661193848})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.3654329776763916})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.5052329301834106})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.4781310558319092})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.5320088863372803})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.509016752243042})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8166, 'crossentropy': 1.29671689453125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 14385], ['id', 10481], ['id', 48102], ['id', 28920], ['id', 48824]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.1989439961337496, 2.1711573134529667, 2.9923243489476103, 3.601443235271014, 4.001000419832703]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.2406110763549805})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.2996492385864258})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.4158172607421875})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.4196460247039795})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.6769251823425293})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.7792060375213623})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8169, 'crossentropy': 1.2654265625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 26034], ['id', 16549], ['id', 32427], ['id', 59362], ['id', 57806]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.105761108184034, 2.09257804618933, 2.9144668158866054, 3.551994441718116, 3.9811843145685604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.1094495058059692})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.114369511604309})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2042784690856934})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.287652611732483})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.5268278121948242})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.407336711883545})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8586, 'crossentropy': 1.0455736328125}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 25644], ['id', 16022], ['id', 7190], ['id', 51653], ['id', 22167]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.1057859636487455, 2.102861395568888, 2.933236673197875, 3.5583592506193584, 3.980944228700551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9999746084213257})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0281299352645874})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0513744354248047})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.132645606994629})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1460702419281006})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2712993621826172})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.27207612991333})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2713358402252197})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8792, 'crossentropy': 1.03669560546875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 53170], ['id', 1127], ['id', 3498], ['id', 17710], ['id', 31090]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.112706615218935, 2.1357855900850824, 3.0295757088186868, 3.668233235669697, 4.058950235150707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9466213583946228})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9142546653747559})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8712705373764038})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9498867392539978})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9956486821174622})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9860732555389404})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8868, 'crossentropy': 0.782963134765625}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 11441], ['id', 35401], ['id', 49493], ['id', 22811], ['id', 34520]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.1478517484462218, 2.13944660223874, 2.911301110377969, 3.5123640347415153, 3.920484179371452]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9496815204620361})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7775954604148865})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9853549003601074})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9902441501617432})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0239614248275757})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8796, 'crossentropy': 0.720122314453125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 11202], ['id', 58560], ['id', 17131], ['id', 15551], ['id', 59339]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0290970140275646, 1.921102816478018, 2.674303220927068, 3.2706002467752233, 3.7158442983278865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8955109119415283})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8742071390151978})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8166059255599976})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8950431942939758})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7949361205101013})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8205509185791016})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.91009521484375})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9029265642166138})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9161489009857178})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8512597680091858})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8668893575668335})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0601550340652466})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0781594514846802})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0296034812927246})
store['active_learning_steps'][15]['training']['best_epoch']=11
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8978, 'crossentropy': 0.779721875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 52462], ['id', 51019], ['id', 5129], ['id', 1376], ['id', 2611]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.19331892482674, 2.3158951112937114, 3.2256488728963966, 3.8359302913254076, 4.216355197153668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0064786672592163})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6968047022819519})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8368560075759888})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9013926982879639})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.845406174659729})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8030002117156982})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8401961326599121})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8854003548622131})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8328683376312256})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9672380089759827})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9386084079742432})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8901636600494385})
store['active_learning_steps'][16]['training']['best_epoch']=9
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.907, 'crossentropy': 0.75314775390625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 24479], ['id', 28512], ['id', 17494], ['id', 2064], ['id', 19574]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.2371309841204616, 2.377545708044538, 3.2754693267917503, 3.8781515310714454, 4.224324520733388]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8329124450683594})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7710431814193726})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8485833406448364})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.886813759803772})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0114655494689941})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8949, 'crossentropy': 0.677547265625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 15472], ['id', 39656], ['id', 1674], ['id', 42206], ['id', 30646]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.9557573049445693, 1.8195933165489695, 2.545407075052341, 3.105919140655585, 3.5277678167360422]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0839999914169312})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7265827655792236})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7980914115905762})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8276495933532715})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8429448008537292})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.799295961856842})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.895882248878479})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9924100041389465})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9263360500335693})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.891, 'crossentropy': 0.77348876953125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 36810], ['id', 9180], ['id', 17318], ['id', 17010], ['id', 11539]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.2100313100938624, 2.3112269611953806, 3.1706803545316804, 3.7792389882006088, 4.14721230427288]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9146966934204102})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.715983510017395})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7218663692474365})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7464160323143005})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8813071250915527})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8898, 'crossentropy': 0.677495703125}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 14649], ['id', 51764], ['id', 57507], ['id', 55128], ['id', 27898]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9227954759849109, 1.7195308533274334, 2.433844650367245, 3.0230963886439914, 3.4630379626060313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.066068172454834})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8562936782836914})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8173719048500061})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.863300085067749})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8204116821289062})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8521398305892944})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8803113698959351})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.018934965133667})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9945583939552307})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8952, 'crossentropy': 0.79296884765625}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 28536], ['id', 29791], ['id', 16488], ['id', 1512], ['id', 46368]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.2533390606094548, 2.276095733991041, 3.1495020999687515, 3.7301224809064344, 4.112694844847246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9810628294944763})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7293939590454102})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6976721882820129})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7286860346794128})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8025015592575073})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6996830701828003})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9020586013793945})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.981029748916626})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8388966917991638})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9101, 'crossentropy': 0.63001865234375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 6466], ['id', 16406], ['id', 45944], ['id', 47068], ['id', 22272]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.108793138744999, 2.0781043622164947, 2.887130263740511, 3.5229017993585616, 3.943062501116448]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.238785982131958})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8235976696014404})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7612528204917908})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8199623823165894})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8214311599731445})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9989224672317505})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9545719623565674})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8730239868164062})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9917272329330444})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0532114505767822})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9573067426681519})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8901, 'crossentropy': 0.801654296875}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 37574], ['id', 60], ['id', 35606], ['id', 18398], ['id', 27183]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1396076327262021, 2.21458745227095, 3.088293965317636, 3.713088842966652, 4.10473068116279]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.084222674369812})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7460784316062927})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6962630748748779})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7912399768829346})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7860085964202881})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.763970136642456})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9262009859085083})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.953626275062561})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8523048758506775})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9886261224746704})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9716538190841675})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.945773184299469})
store['active_learning_steps'][23]['training']['best_epoch']=9
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9087, 'crossentropy': 0.6849658203125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 53872], ['id', 50743], ['id', 9557], ['id', 20037], ['id', 33505]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.145324779629242, 2.153358058527611, 2.9975172954049967, 3.638793268267733, 4.039846232125555]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.15574312210083})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8482477068901062})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7000453472137451})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7852360606193542})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8805975914001465})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7769599556922913})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7805728316307068})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8310545086860657})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7911570072174072})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.912, 'crossentropy': 0.674663232421875}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 31301], ['id', 43745], ['id', 16756], ['id', 50930], ['id', 33705]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0460058259869451, 2.022652020932466, 2.8275963537180653, 3.4820293334636725, 3.9241882887304795]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0976221561431885})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6712619662284851})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6084912419319153})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6095646023750305})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6104341745376587})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.559482216835022})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6465499401092529})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6180680990219116})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6512587666511536})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9287, 'crossentropy': 0.525444091796875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 40466], ['id', 21952], ['id', 52169], ['id', 49002], ['id', 16511]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0740988921056849, 2.07523915991673, 2.917448609025489, 3.5321368444595027, 3.948247169058167]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.1735832691192627})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.693095862865448})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6102747917175293})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5726121068000793})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6797049045562744})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6177768707275391})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5747910737991333})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9344, 'crossentropy': 0.494559716796875}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 36984], ['id', 54896], ['id', 48681], ['id', 47643], ['id', 42085]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9811453383657436, 1.9014719425541973, 2.6753709422135854, 3.288052913511896, 3.753190420261909]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.1128780841827393})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6532042026519775})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.552200436592102})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.527084469795227})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5763732194900513})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5080254077911377})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5617641806602478})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5850687026977539})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5837126970291138})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5954889059066772})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9355, 'crossentropy': 0.500622607421875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 43126], ['id', 31738], ['id', 37367], ['id', 7867], ['id', 28192]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.1801790562566443, 2.2008988335929818, 3.0442155850303614, 3.660939383720848, 4.062067292460573]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.3594096899032593})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6977310180664062})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5601115226745605})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6096801161766052})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5749523639678955})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.556167721748352})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5863640904426575})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6633684635162354})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5825758576393127})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5819153785705566})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6044508218765259})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6821704506874084})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6627655029296875})
store['active_learning_steps'][28]['training']['best_epoch']=10
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.927, 'crossentropy': 0.54956904296875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 59314], ['id', 39668], ['id', 45988], ['id', 16446], ['id', 37450]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.29976647162168, 2.3395865722055045, 3.195720939657278, 3.795977025993013, 4.160861918484049]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.3110814094543457})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7538164258003235})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6526104807853699})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6395971179008484})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.702775239944458})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7102020382881165})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6516147255897522})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.597176513671875}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 22083], ['id', 16836], ['id', 46412], ['id', 49616], ['id', 36818]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.0071786984341136, 1.9495697564176244, 2.6886471895460744, 3.286902428320227, 3.720478802551482]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.319727897644043})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6538749933242798})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.61540287733078})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5486537218093872})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6185839176177979})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6298821568489075})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6072670221328735})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6271178126335144})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6624575853347778})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6684184074401855})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6869145035743713})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.550463916015625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 21426], ['id', 42415], ['id', 38657], ['id', 56414], ['id', 2859]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.052941138890239, 2.0168367462835803, 2.8245343797783153, 3.450141869760751, 3.8962768529613694]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.3804848194122314})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6949438452720642})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5426290035247803})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5640983581542969})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5646581649780273})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5506938695907593})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5629024505615234})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6003259420394897})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6405032873153687})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9313, 'crossentropy': 0.473532080078125}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 26444], ['id', 11572], ['id', 250], ['id', 55244], ['id', 11737]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.084050743810379, 2.0916980103353664, 2.905203594625563, 3.5152320409525837, 3.927570819823732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0995477437973022})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6070783138275146})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5364230871200562})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5947191715240479})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5768193006515503})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5122057795524597})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5949169397354126})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5783084630966187})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5776823163032532})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9344, 'crossentropy': 0.473232275390625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 25384], ['id', 17079], ['id', 52358], ['id', 31456], ['id', 58832]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9949647732099389, 1.918745020059923, 2.751191635018227, 3.4160550333370967, 3.8627360662538512]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.285989761352539})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7843929529190063})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.58916175365448})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6344665288925171})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6330686807632446})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5820360779762268})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5853826999664307})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6217091679573059})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6228757500648499})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6522458791732788})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5871566534042358})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7131054401397705})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9346, 'crossentropy': 0.510773974609375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 59731], ['id', 2381], ['id', 27358], ['id', 39561], ['id', 42199]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0849964809311652, 2.051287424964999, 2.880563241618008, 3.5199276493794827, 3.9513522760595734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.2002235651016235})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7247252464294434})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6114321947097778})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5798630714416504})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6458524465560913})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5262029767036438})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5899964570999146})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9265, 'crossentropy': 0.5155509765625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 57728], ['id', 37469], ['id', 59747], ['id', 32926], ['id', 50789]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8935346218073517, 1.7091139904015513, 2.4470386873958017, 3.059166067601299, 3.5299425287092188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.308307409286499})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.701058030128479})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5330134630203247})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.49556964635849})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5450468063354492})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5470799803733826})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5328313112258911})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9341, 'crossentropy': 0.47046220703125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 54542], ['id', 34639], ['id', 13942], ['id', 48973], ['id', 12497]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9419319226600664, 1.7583899226133108, 2.513687380251403, 3.113098268105266, 3.5652432523482727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.374168038368225})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.649217963218689})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.579800009727478})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5781396627426147})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.496914803981781})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5277652740478516})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5857526063919067})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5346566438674927})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5066730976104736})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5460385084152222})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5487165451049805})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5752694606781006})
store['active_learning_steps'][36]['training']['best_epoch']=9
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9383, 'crossentropy': 0.492097216796875}
