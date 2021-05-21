store = {}
store['timestamp']=1621471682
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=3']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=3
store['worker_id']=3
store['num_workers']=80
store['config']={'seed': 1237, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.2208540439605713})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.690932512283325})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.9579710960388184})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.031991720199585})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.7753758430480957})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.5379538536071777})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.1273884773254395})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.190985918045044})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.650599241256714})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.607813835144043})
store['active_learning_steps'][0]['training']['best_epoch']=7
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6101, 'crossentropy': 3.36756640625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.6820123195648193})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.7366827726364136})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.6262285709381104})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.6489226818084717})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 22481], ['id', 4014], ['id', 26279], ['id', 1477], ['id', 29303]], 'labels': [-1, -1, 6, -1, -1], 'scores': [1.0486369128463235, 1.7914864470021858, 2.2654640665320365, 2.5388699232628538, 2.723550070398809]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.1816627979278564})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.094057559967041})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.043717861175537})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.5747032165527344})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.216386318206787})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.3560938835144043})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5872, 'crossentropy': 3.217316796875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.8346636295318604})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.679711103439331})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.7275965213775635})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.7014625072479248})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.703977108001709})
store['active_learning_steps'][1]['eval_training']['best_epoch']=5
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 36148], ['id', 46852], ['id', 5388], ['id', 47256], ['id', 48121]], 'labels': [-1, -1, 5, -1, -1], 'scores': [0.9665453863165279, 1.7137598027844887, 2.2205480965307616, 2.592395972479752, 2.8267649163657786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.4631824493408203})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.8892550468444824})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.0768144130706787})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.1967530250549316})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.57387113571167})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.5765938758850098})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.497437000274658})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.5060367584228516})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.934142589569092})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.7077102661132812})
store['active_learning_steps'][2]['training']['best_epoch']=7
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6155, 'crossentropy': 3.855665625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.7491052150726318})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.8392314910888672})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.7772917747497559})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.803228735923767})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.9263319969177246})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.013718605041504})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.9272501468658447})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 3398], ['id', 46864], ['id', 55402], ['id', 50296], ['id', 20878]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2468905110608435, 2.168227718628689, 2.7384149799235935, 3.122866806607141, 3.336739876140659]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.2249317169189453})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.6291701793670654})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.043531894683838})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.147859573364258})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.2901387214660645})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.196556568145752})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.9576423168182373})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.8577351570129395})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.2859268188476562})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6257, 'crossentropy': 3.32788046875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.7368080615997314})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.6345601081848145})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.555311679840088})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.514615535736084})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.5383113622665405})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.561516284942627})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.6755592823028564})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.502432107925415})
store['active_learning_steps'][3]['eval_training']['best_epoch']=7
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 36197], ['id', 20564], ['id', 7008], ['id', 41166], ['id', 33026]], 'labels': [-1, -1, -1, 3, 7], 'scores': [1.1479199034493839, 2.0731816003697547, 2.6940683128309284, 3.0892674708712793, 3.311550328593119]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.0475149154663086})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.5404677391052246})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.643308162689209})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.904849052429199})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.191124439239502})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6163, 'crossentropy': 2.649615625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.548706293106079})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.6089413166046143})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.5684850215911865})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.5467158555984497})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 2281], ['id', 2360], ['id', 56427], ['id', 26174], ['id', 48195]], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.9328575810223654, 1.6263637202776713, 2.0834190879676058, 2.3592767546292484, 2.5319465674851473]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.1181180477142334})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.4214463233947754})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.778623104095459})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.8419265747070312})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.1019654273986816})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.7635746002197266})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.39017915725708})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.1935038566589355})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.6036596298217773})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.19996976852417})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.409754753112793})
store['active_learning_steps'][5]['training']['best_epoch']=8
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.63, 'crossentropy': 3.51633046875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.928203821182251})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.7254650592803955})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.872549295425415})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.9228055477142334})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.9082999229431152})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.7697219848632812})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.8110601902008057})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.788948655128479})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.7616558074951172})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.7938852310180664})
store['active_learning_steps'][5]['eval_training']['best_epoch']=9
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 35578], ['id', 56394], ['id', 16200], ['id', 58408], ['id', 15568]], 'labels': [-1, 2, -1, -1, -1], 'scores': [1.1114045137054183, 1.9428571739048996, 2.6213662222552125, 3.0411784104029516, 3.2524424003511188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.8406203985214233})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.779599189758301})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.646012783050537})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.0239195823669434})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6139, 'crossentropy': 1.9353328125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2827993631362915})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.2151625156402588})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.230488657951355})
store['active_learning_steps'][6]['eval_training']['best_epoch']=1
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 26441], ['id', 23564], ['id', 50317], ['id', 30678], ['id', 41636]], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.7632547694193834, 1.2885601884416755, 1.710821412211562, 2.0036263761616775, 2.1273694993107846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.9657599925994873})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.4753518104553223})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.69368839263916})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.7833614349365234})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.854267120361328})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.723478317260742})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.9121603965759277})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.196840763092041})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6262, 'crossentropy': 3.0766126953125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.7017313241958618})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.8392857313156128})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.7047595977783203})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.8174107074737549})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.5984714031219482})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 4850], ['id', 49503], ['id', 29908], ['id', 777], ['id', 49479]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.0590789543309058, 1.8488285043801844, 2.4009039558407848, 2.7528410427834284, 2.9232129319338975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.6837379932403564})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.341820240020752})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.53802752494812})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.360495090484619})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.5040669441223145})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.8001818656921387})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.812905788421631})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.7980358600616455})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6665, 'crossentropy': 2.7359669921875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.8811407089233398})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.023550033569336})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.7606476545333862})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.9222629070281982})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.958204984664917})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 18227], ['id', 20955], ['id', 31892], ['id', 50154], ['id', 50377]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.289039983273459, 2.239110110235008, 2.888288955410901, 3.226809272471978, 3.424513515403472]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.7622982263565063})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.2475552558898926})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.8712732791900635})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.633378028869629})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.7114768028259277})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6493, 'crossentropy': 2.4224740234375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.4730749130249023})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.520436406135559})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3854095935821533})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3780643939971924})
store['active_learning_steps'][9]['eval_training']['best_epoch']=1
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 2390], ['id', 27181], ['id', 24035], ['id', 12183], ['id', 12967]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8824739417732916, 1.596384540201087, 2.0968517297356786, 2.3534961180223846, 2.4752126492101594]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.8878862857818604})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.359144687652588})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.047991991043091})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.154384136199951})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.9067296981811523})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6288, 'crossentropy': 2.5240638671875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.5824956893920898})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.5148638486862183})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3698655366897583})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3055689334869385})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 6616], ['id', 4905], ['id', 33754], ['id', 9779], ['id', 38015]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0388285193525375, 1.7861286110006112, 2.352131713645065, 2.6678624102629023, 2.8588285808867484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.6773567199707031})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.383603096008301})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.824094533920288})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.3106436729431152})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.871521234512329})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.96307635307312})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.0916152000427246})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.163407564163208})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.63, 'crossentropy': 3.160062109375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.6360934972763062})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.6392109394073486})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.5923064947128296})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.5665048360824585})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.5906908512115479})
store['active_learning_steps'][11]['eval_training']['best_epoch']=2
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 48200], ['id', 11784], ['id', 46619], ['id', 17440], ['id', 48158]], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.9153975866839653, 1.626127310591667, 2.1200092046299313, 2.4594833806612844, 2.640480863229657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.8145190477371216})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.2013845443725586})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.543790340423584})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.6090240478515625})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.713076114654541})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.816481113433838})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.956655979156494})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6365, 'crossentropy': 2.8113068359375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.7426048517227173})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.935745358467102})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.557299256324768})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.816795825958252})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.668218970298767})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.6981565952301025})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 36283], ['id', 51650], ['id', 22717], ['id', 11535], ['id', 45282]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0446238740766909, 1.8809304603605237, 2.4746749114172912, 2.8510353829694086, 3.081747650190364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.9643898010253906})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.3918232917785645})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3275747299194336})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.575465202331543})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.800891399383545})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6522, 'crossentropy': 2.247941015625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.6521296501159668})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.479591727256775})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.311302661895752})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.3380765914916992})
store['active_learning_steps'][13]['eval_training']['best_epoch']=2
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 58163], ['id', 32818], ['id', 46992], ['id', 13134], ['id', 35802]], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.8068521485643911, 1.437892910626615, 1.9257525077761963, 2.2374531656713375, 2.4443680989023306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.7139966487884521})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.4404962062835693})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6550869941711426})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.9638054370880127})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6305, 'crossentropy': 1.923782421875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3709323406219482})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2911467552185059})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2485227584838867})
store['active_learning_steps'][14]['eval_training']['best_epoch']=2
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 22679], ['id', 40623], ['id', 5490], ['id', 16849], ['id', 41696]], 'labels': [-1, -1, 0, -1, 5], 'scores': [0.7812866827940008, 1.411483001939581, 1.8858800958009443, 2.1983369438144296, 2.404820231413362]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.7554093599319458})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.3511362075805664})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.612874984741211})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.51670503616333})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.962195634841919})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.3186163902282715})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.2164864540100098})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.1913094520568848})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6344, 'crossentropy': 3.0915150390625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.7857036590576172})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.5933393239974976})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.604601502418518})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.5861989259719849})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.6789636611938477})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.556653618812561})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.6401846408843994})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 5010], ['id', 17088], ['id', 18506], ['id', 19809], ['id', 39989]], 'labels': [-1, -1, -1, 6, 9], 'scores': [1.0289169394748028, 1.8159581446505269, 2.329444911049779, 2.665843721242068, 2.845036279472174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.686201572418213})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.116940498352051})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.466856002807617})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.4781551361083984})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.6799206733703613})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6539, 'crossentropy': 2.3251123046875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.4428317546844482})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.5010626316070557})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3365771770477295})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.4083659648895264})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 48323], ['id', 31624], ['id', 57619], ['id', 59777], ['id', 38920]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.080835463628905, 1.7959394931700094, 2.311505440578504, 2.6079753504455994, 2.7490898295956194]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.8281965255737305})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.429168462753296})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.662087917327881})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.6147148609161377})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.8927717208862305})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.8549985885620117})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.102957248687744})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6309, 'crossentropy': 2.867755859375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.6132850646972656})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.7350938320159912})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.7028815746307373})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.6514272689819336})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.807431697845459})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.699060082435608})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 58172], ['id', 18194], ['id', 21601], ['id', 44835], ['id', 13734]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.1634164033048862, 2.0675258179789715, 2.6052050321652924, 2.9584611597828436, 3.1869404596076603]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.6052300930023193})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.0767571926116943})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.5748026371002197})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.7366695404052734})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.6182522773742676})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.977356433868408})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.242154598236084})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.1616101264953613})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6477, 'crossentropy': 2.9555208984375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.783879041671753})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.8473784923553467})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.7660140991210938})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.7182964086532593})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.662705898284912})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.682572364807129})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.648393988609314})
store['active_learning_steps'][18]['eval_training']['best_epoch']=7
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 8714], ['id', 42934], ['id', 17212], ['id', 48045], ['id', 48425]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0026325002507641, 1.800314044180094, 2.3970466765646985, 2.7308032626316088, 2.9164219576044115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.6420495510101318})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.187880516052246})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.287027359008789})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.438114881515503})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.642, 'crossentropy': 1.7522685546875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2770066261291504})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1894962787628174})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1672509908676147})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 40258], ['id', 6944], ['id', 46757], ['id', 56355], ['id', 33773]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.9433707652101853, 1.6669904554574284, 2.150639806177513, 2.447930724679088, 2.5865254157634183]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.6573758125305176})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.238368034362793})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.3137869834899902})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6576945781707764})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.007192611694336})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.0190019607543945})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6406, 'crossentropy': 2.619410546875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.5268878936767578})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.4090214967727661})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.449706792831421})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3950309753417969})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3608264923095703})
store['active_learning_steps'][20]['eval_training']['best_epoch']=2
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 27051], ['id', 18763], ['id', 39325], ['id', 20322], ['id', 8877]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.069638511212815, 1.7864814277385603, 2.2666264478535125, 2.566355277132822, 2.733369926786927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.6315263509750366})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.190528392791748})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.3381094932556152})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.4370439052581787})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.821460723876953})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.006453037261963})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.954632043838501})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.905987501144409})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.65, 'crossentropy': 2.929015234375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.3358913660049438})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.4653165340423584})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.5010895729064941})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.4052395820617676})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.4279906749725342})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.4174044132232666})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.4524319171905518})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 16426], ['id', 39333], ['id', 17777], ['id', 30350], ['id', 54507]], 'labels': [-1, 2, -1, 2, -1], 'scores': [1.255600031609196, 2.0946133156660576, 2.7018184614445513, 3.0879141912048667, 3.2753002246750653]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.8406000137329102})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.3510634899139404})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.579418182373047})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.724900960922241})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.8092594146728516})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.8404054641723633})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.249809741973877})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.3924367427825928})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6468, 'crossentropy': 3.096291796875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.5166637897491455})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.829210638999939})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.8295683860778809})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.9072635173797607})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.01338529586792})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.7887651920318604})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.810760498046875})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 10258], ['id', 21911], ['id', 32992], ['id', 22673], ['id', 49064]], 'labels': [-1, -1, 6, -1, -1], 'scores': [0.9883021389419373, 1.7377888147639933, 2.270112541094443, 2.634035332905966, 2.834095748209871]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.6064274311065674})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.162846565246582})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.405325412750244})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.3049864768981934})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.9450225830078125})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.6698546409606934})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 3.0260066986083984})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.8994359970092773})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.008936882019043})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.999189853668213})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.65, 'crossentropy': 3.162719921875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.5455232858657837})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.6500115394592285})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.743970513343811})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.676066517829895})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.661712408065796})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.6229588985443115})
store['active_learning_steps'][23]['eval_training']['best_epoch']=3
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 8948], ['id', 28016], ['id', 36858], ['id', 9425], ['id', 4875]], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.0161626397943886, 1.7630163864420005, 2.2761337339595373, 2.599969274283935, 2.780493703738675]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.4866310358047485})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.9555236101150513})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.6016435623168945})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.5826587677001953})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.9625964164733887})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6437, 'crossentropy': 2.1490115234375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.4278333187103271})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2817670106887817})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3154520988464355})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3009381294250488})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 52453], ['id', 53863], ['id', 2835], ['id', 56173], ['id', 39586]], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.9375302144722424, 1.5638153807114499, 2.0032251524690707, 2.236863629677252, 2.375405950134911]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.510932207107544})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.0313491821289062})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.3720765113830566})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.418544292449951})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.7523152828216553})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.997687339782715})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.9197514057159424})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6419, 'crossentropy': 2.6213623046875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.4030506610870361})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.451000690460205})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.53139066696167})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.5694057941436768})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.6151450872421265})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.4943504333496094})
store['active_learning_steps'][25]['eval_training']['best_epoch']=3
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 45218], ['id', 8551], ['id', 24738], ['id', 19136], ['id', 10453]], 'labels': [-1, -1, 3, 8, -1], 'scores': [0.936233202542359, 1.622020798649731, 2.0941536429594314, 2.3573754928344917, 2.4890324110026536]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.5530369281768799})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.030759334564209})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.4254310131073})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.603997230529785})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.830756664276123})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.6197164058685303})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.6489508152008057})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.2399210929870605})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9912912845611572})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6495, 'crossentropy': 2.882366015625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4162299633026123})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.572192907333374})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.7195215225219727})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.565176010131836})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.7310413122177124})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.6353263854980469})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 34928], ['id', 45942], ['id', 43054], ['id', 12896], ['id', 53977]], 'labels': [-1, -1, 6, 0, -1], 'scores': [1.081880321529769, 1.7752251921173303, 2.182315333211998, 2.441489796316615, 2.58942899805009]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.5293490886688232})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.3473024368286133})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.268155574798584})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.022942066192627})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.465174674987793})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.0457401275634766})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6391, 'crossentropy': 2.4883947265625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.4256916046142578})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.5209141969680786})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3508999347686768})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3767319917678833})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2865116596221924})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 48712], ['id', 51163], ['id', 934], ['id', 10469], ['id', 36020]], 'labels': [-1, 0, -1, -1, -1], 'scores': [1.013393182820321, 1.8206094725863726, 2.3562240094518425, 2.6837040986703533, 2.8464903289473145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.5108952522277832})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.1266210079193115})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.496845245361328})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.7336785793304443})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.592000961303711})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.2232747077941895})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.957674503326416})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.028170585632324})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6448, 'crossentropy': 2.8779591796875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.541670322418213})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.6519227027893066})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.556457757949829})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.635030746459961})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.6814134120941162})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.6730222702026367})
store['active_learning_steps'][28]['eval_training']['best_epoch']=3
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 8455], ['id', 58344], ['id', 30725], ['id', 36867], ['id', 12121]], 'labels': [-1, -1, 0, 5, 1], 'scores': [1.0134436734824839, 1.8209284679103492, 2.28303592608275, 2.6155767521863007, 2.8120925450096013]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.5636625289916992})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.1148667335510254})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.463064193725586})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.863283395767212})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.868054151535034})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.6012537479400635})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6468, 'crossentropy': 2.5996673828125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.528098702430725})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4780454635620117})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.442549705505371})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.5514750480651855})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4253380298614502})
store['active_learning_steps'][29]['eval_training']['best_epoch']=3
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 41014], ['id', 31183], ['id', 17205], ['id', 50389], ['id', 29292]], 'labels': [-1, -1, 7, 0, -1], 'scores': [0.8804545032998388, 1.571816557385957, 2.064764770973631, 2.336994610422031, 2.4846628573744347]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.5389833450317383})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.825939655303955})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.179598331451416})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.3768911361694336})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.736374855041504})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.527341842651367})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.0568532943725586})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 3.2194132804870605})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6644, 'crossentropy': 2.8486626953125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3794268369674683})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.6228282451629639})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.657285213470459})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.5763447284698486})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.5373940467834473})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.6909635066986084})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.4961555004119873})
store['active_learning_steps'][30]['eval_training']['best_epoch']=4
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 53475], ['id', 33276], ['id', 32270], ['id', 33505], ['id', 54798]], 'labels': [-1, 8, 6, -1, -1], 'scores': [0.9543910945021196, 1.6304710602702066, 2.1932086715282186, 2.609809504494553, 2.873906627369066]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.4348735809326172})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.8656108379364014})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.215458869934082})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.392564296722412})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.5529003143310547})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.510756254196167})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.7657840251922607})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.159461498260498})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.949972152709961})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6651, 'crossentropy': 2.7401306640625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.284184455871582})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.5079553127288818})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.685255527496338})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.595747947692871})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.6304123401641846})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.6315724849700928})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.5033632516860962})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.6341338157653809})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 18665], ['id', 22894], ['id', 38429], ['id', 45831], ['id', 39918]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.09325159170423, 1.9889015667290846, 2.5483894784579473, 2.9127311911622193, 3.0958640382341205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.6496429443359375})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.0062365531921387})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.388632297515869})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.433590888977051})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.6416029930114746})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5725512504577637})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.8124301433563232})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.098663806915283})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 3.100667953491211})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 3.0015478134155273})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.1998987197875977})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.3383913040161133})
store['active_learning_steps'][32]['training']['best_epoch']=9
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6484, 'crossentropy': 3.295355859375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.449737548828125})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.6745150089263916})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.6228938102722168})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.7274510860443115})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.7214634418487549})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.6604225635528564})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.5919244289398193})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.623913288116455})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.6829912662506104})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.6175646781921387})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.8092622756958008})
store['active_learning_steps'][32]['eval_training']['best_epoch']=10
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 19369], ['id', 48212], ['id', 57100], ['id', 5052], ['id', 53026]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2837679494052368, 2.1756131344913414, 2.816671246932059, 3.168806355111972, 3.372890970019318]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.7165095806121826})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.8603928089141846})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.295682430267334})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.564183235168457})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.3840718269348145})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.1350085735321045})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 3.063232421875})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 3.3123769760131836})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.5208024978637695})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.4285168647766113})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.685171127319336})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6667, 'crossentropy': 3.31504140625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3603678941726685})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.5568283796310425})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.5772216320037842})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.6330296993255615})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.6062533855438232})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.6039676666259766})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.5874919891357422})
store['active_learning_steps'][33]['eval_training']['best_epoch']=4
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 54068], ['id', 17358], ['id', 34332], ['id', 5750], ['id', 14006]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.181952551391352, 2.02486676039931, 2.588440242877129, 2.9337629029903747, 3.117495566294265]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.4268949031829834})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.8248103857040405})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.2028074264526367})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.369326591491699})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.355404853820801})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.5676496028900146})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.7284464836120605})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.55609130859375})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.5964457988739014})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.0551390647888184})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.921009063720703})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.888336181640625})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 3.0556530952453613})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 3.02016019821167})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.10139536857605})
store['active_learning_steps'][34]['training']['best_epoch']=12
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6735, 'crossentropy': 3.0835328125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.5902544260025024})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.4955015182495117})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.7196027040481567})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.6393532752990723})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.8067022562026978})
store['active_learning_steps'][34]['eval_training']['best_epoch']=2
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 32276], ['id', 22159], ['id', 10249], ['id', 20650], ['id', 56585]], 'labels': [-1, 2, -1, 4, -1], 'scores': [1.02849614926068, 1.7876945885823603, 2.3471776862248506, 2.667641822835309, 2.8260098640371]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.465407371520996})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.0707483291625977})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.055875778198242})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.359799861907959})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.5207509994506836})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.302366256713867})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.4819083213806152})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.0064754486083984})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.832284927368164})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.9259238243103027})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6675, 'crossentropy': 2.6679787109375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.4361491203308105})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4486794471740723})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.5160009860992432})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.498702049255371})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4710702896118164})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.508786678314209})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.451092004776001})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4917654991149902})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.490599274635315})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 48865], ['id', 27900], ['id', 32328], ['id', 25243], ['id', 21066]], 'labels': [-1, -1, -1, 5, 6], 'scores': [1.0263891953845214, 1.7106330745913474, 2.196264883037592, 2.543424533407909, 2.7452140922771684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.4939022064208984})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.828214168548584})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.027733325958252})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.3757176399230957})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.4709925651550293})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6231932640075684})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6557, 'crossentropy': 2.221280859375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.501157283782959})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4778465032577515})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.4687659740447998})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.5403082370758057})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.4379098415374756})
store['active_learning_steps'][36]['eval_training']['best_epoch']=4
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 30614], ['id', 6185], ['id', 49094], ['id', 24098], ['id', 5496]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8821498767193618, 1.5916990358682073, 2.0115913215787566, 2.316962748762327, 2.480193975322554]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.452066421508789})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.7160736322402954})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.160266399383545})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.2301533222198486})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.681060552597046})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.814920425415039})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.7809152603149414})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.654, 'crossentropy': 2.39814453125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3507137298583984})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3717166185379028})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3149197101593018})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.3365999460220337})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3592915534973145})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2982109785079956})
store['active_learning_steps'][37]['eval_training']['best_epoch']=6
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 5398], ['id', 6863], ['id', 6236], ['id', 43102], ['id', 43722]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1724625014945604, 1.9242423785565343, 2.4532629503283987, 2.7657381819539903, 2.9772132489124274]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.5199363231658936})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.927558422088623})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.091130018234253})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.492633819580078})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.4596757888793945})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.830869197845459})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6606979370117188})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6524, 'crossentropy': 2.7137689453125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.551850438117981})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.4622523784637451})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.4100265502929688})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3516368865966797})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.432194709777832})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.4155232906341553})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 13954], ['id', 9610], ['id', 23229], ['id', 50424], ['id', 16295]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.1161612570182111, 1.9848679000178717, 2.474125046614321, 2.668904543075879, 2.7839865580156706]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.4302157163619995})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.9016185998916626})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.1424055099487305})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.256279945373535})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6665682792663574})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.5833213329315186})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.5888843536376953})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.904632568359375})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.0513477325439453})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.9946517944335938})
store['active_learning_steps'][39]['training']['best_epoch']=7
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6595, 'crossentropy': 2.999479296875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3446999788284302})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.467604637145996})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.352647304534912})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.3499562740325928})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.4023211002349854})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.312084436416626})
store['active_learning_steps'][39]['eval_training']['best_epoch']=3
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 14074], ['id', 47625], ['id', 26323], ['id', 1083], ['id', 10646]], 'labels': [-1, -1, 6, -1, 8], 'scores': [0.9242436350724388, 1.6675283348254064, 2.0694865573797108, 2.31018842257396, 2.430467453302673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4270864725112915})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.6082745790481567})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.9471482038497925})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.0153324604034424})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.3564581871032715})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6685, 'crossentropy': 1.7541775390625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.215165615081787})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1670281887054443})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1567885875701904})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1119961738586426})
store['active_learning_steps'][40]['eval_training']['best_epoch']=3
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 12645], ['id', 59177], ['id', 35606], ['id', 44174], ['id', 45875]], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.9021712831601798, 1.5457312731872324, 1.9713505494788652, 2.1958148244438416, 2.3068913394783035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4085874557495117})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.7172571420669556})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.955784559249878})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.9234848022460938})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.3706674575805664})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3965139389038086})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.696166753768921})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6546, 'crossentropy': 2.067489453125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3768441677093506})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.4037940502166748})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3518129587173462})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3198940753936768})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.286813735961914})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3137218952178955})
store['active_learning_steps'][41]['eval_training']['best_epoch']=3
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 10921], ['id', 46447], ['id', 5314], ['id', 28102], ['id', 50479]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8586589041181467, 1.6109112000932346, 2.0754351097499137, 2.3244038346442757, 2.500126794124699]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.437342643737793})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.5795016288757324})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.9271149635314941})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.0151991844177246})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.226520538330078})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.307188034057617})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.5915818214416504})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.432891368865967})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.6853957176208496})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6636, 'crossentropy': 2.5808140625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.3501992225646973})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.4391096830368042})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.530474305152893})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.5131256580352783})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.4325575828552246})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3936859369277954})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.4054198265075684})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.381969928741455})
store['active_learning_steps'][42]['eval_training']['best_epoch']=5
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 5632], ['id', 35859], ['id', 19764], ['id', 18166], ['id', 665]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0839189043440502, 1.9767002095635315, 2.5632138710864893, 2.8763558103082802, 3.0580299294704147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.571385145187378})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.6638339757919312})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.884376049041748})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.0125389099121094})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.0157582759857178})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.681816577911377})
store['active_learning_steps'][43]['training']['best_epoch']=3
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6587, 'crossentropy': 2.0248177734375}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2575008869171143})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.3740334510803223})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.4336631298065186})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.358255386352539})
store['active_learning_steps'][43]['eval_training']['best_epoch']=1
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 31201], ['id', 42986], ['id', 45422], ['id', 28237], ['id', 30482]], 'labels': [-1, -1, -1, 0, 2], 'scores': [0.936650073752793, 1.6581651532351254, 2.1105643368102713, 2.302117678343352, 2.3761615452922618]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.46843683719635})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.795898199081421})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.0030126571655273})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.2685186862945557})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.7496109008789062})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.8846287727355957})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.6685791015625})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.510662078857422})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.6294567584991455})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 3.155259132385254})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.1230530738830566})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.832180976867676})
store['active_learning_steps'][44]['training']['best_epoch']=9
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6689, 'crossentropy': 2.6774671875}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.4373624324798584})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2810966968536377})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.4219233989715576})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.4774928092956543})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.4088597297668457})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.3131424188613892})
store['active_learning_steps'][44]['eval_training']['best_epoch']=3
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 43456], ['id', 45149], ['id', 34366], ['id', 56207], ['id', 36800]], 'labels': [-1, -1, -1, 3, -1], 'scores': [0.788787474986484, 1.4924658279252077, 2.015252290776356, 2.3437809014522566, 2.5211839685168242]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.5399607419967651})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.811434268951416})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.9031765460968018})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.1311264038085938})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.503652572631836})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.479436159133911})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.4794559478759766})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.6686267852783203})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.526895046234131})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.7222962379455566})
store['active_learning_steps'][45]['training']['best_epoch']=7
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6585, 'crossentropy': 2.9171525390625}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.432592749595642})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.5064072608947754})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.5190505981445312})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.4829528331756592})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.5147473812103271})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.4815285205841064})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.5115206241607666})
store['active_learning_steps'][45]['eval_training']['best_epoch']=4
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 40350], ['id', 20388], ['id', 27382], ['id', 37377], ['id', 42007]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.074671930666554, 2.0189893355143296, 2.644098206292155, 2.987409041823926, 3.1765287907921804]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.331312656402588})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.6438877582550049})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.0164308547973633})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.0978269577026367})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.2018167972564697})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.4552388191223145})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.6276235580444336})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.8272361755371094})
store['active_learning_steps'][46]['training']['best_epoch']=5
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6678, 'crossentropy': 2.401452734375}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2855955362319946})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.4626808166503906})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.364389419555664})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2947533130645752})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2857303619384766})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2764500379562378})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2572238445281982})
store['active_learning_steps'][46]['eval_training']['best_epoch']=5
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 47998], ['id', 47575], ['id', 28514], ['id', 27540], ['id', 34833]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9626638478988394, 1.764226892996933, 2.3055390402989033, 2.689181462871466, 2.8996194497976298]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.4165735244750977})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.8075402975082397})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.1465210914611816})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.124022960662842})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.279364585876465})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.604294776916504})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.4572525024414062})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.494442939758301})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.8278017044067383})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.7721569538116455})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.8927226066589355})
store['active_learning_steps'][47]['training']['best_epoch']=8
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.653, 'crossentropy': 2.7724302734375}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.38275945186615})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.490623116493225})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4180309772491455})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4681462049484253})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.4139533042907715})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4158775806427002})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.4100172519683838})
store['active_learning_steps'][47]['eval_training']['best_epoch']=4
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 26843], ['id', 30638], ['id', 42832], ['id', 39623], ['id', 37763]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.0227560399683844, 1.8380367503605861, 2.34386124782153, 2.5978331127792735, 2.7244585584666137]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.4820833206176758})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.8143250942230225})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.9705169200897217})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.995058536529541})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.4366931915283203})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.6893227100372314})
store['active_learning_steps'][48]['training']['best_epoch']=3
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6515, 'crossentropy': 1.9316484375}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.296245813369751})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1953105926513672})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.215242862701416})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2419676780700684})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2231632471084595})
store['active_learning_steps'][48]['eval_training']['best_epoch']=2
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 36256], ['id', 14377], ['id', 43623], ['id', 5430], ['id', 50276]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.9747096205320589, 1.7529159556313383, 2.1940360063864603, 2.4830971334218384, 2.64643761088473]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2775084972381592})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.6386802196502686})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.8891494274139404})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.013280153274536})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.2472710609436035})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.2642598152160645})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.6147871017456055})
store['active_learning_steps'][49]['training']['best_epoch']=4
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6607, 'crossentropy': 2.198449609375}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2686619758605957})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2842464447021484})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2659330368041992})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2530139684677124})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.195598840713501})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2426297664642334})
store['active_learning_steps'][49]['eval_training']['best_epoch']=5
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 46295], ['id', 15731], ['id', 842], ['id', 1756], ['id', 55027]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0494053326229358, 1.918322165797775, 2.4899053302886864, 2.832551918878765, 3.0411176996968923]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.473587155342102})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.3876831531524658})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.7979114055633545})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.9833340644836426})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.2911863327026367})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6587, 'crossentropy': 1.472316796875}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.3923377990722656})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1246428489685059})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0974364280700684})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0878357887268066})
store['active_learning_steps'][50]['eval_training']['best_epoch']=3
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 29050], ['id', 21285], ['id', 36202], ['id', 19160], ['id', 10350]], 'labels': [-1, -1, -1, 3, 5], 'scores': [0.7400845681946113, 1.304496579011214, 1.7394463852464463, 1.9917472430731795, 2.1420186908029617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 1.4245178699493408})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.6175763607025146})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.966156244277954})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.018327474594116})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.258538246154785})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.669193744659424})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.357369899749756})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.380415201187134})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.8075387477874756})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.2207260131835938})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.7589192390441895})
store['active_learning_steps'][51]['training']['best_epoch']=8
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6718, 'crossentropy': 2.74224765625}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.413355827331543})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.4743084907531738})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.4740347862243652})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.6458156108856201})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.608475923538208})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.5760796070098877})
store['active_learning_steps'][51]['eval_training']['best_epoch']=3
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 22090], ['id', 13604], ['id', 11274], ['id', 51118], ['id', 7561]], 'labels': [-1, -1, 2, -1, -1], 'scores': [1.310065798894633, 2.244952164815121, 2.9456289530077284, 3.3043289072369273, 3.5118369888167376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3903145790100098})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.7499585151672363})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.9622905254364014})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.093146324157715})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.3555989265441895})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.475238800048828})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.899850368499756})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.9531843662261963})
store['active_learning_steps'][52]['training']['best_epoch']=5
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6468, 'crossentropy': 2.440697265625}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.3873428106307983})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2768794298171997})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4435791969299316})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.4565213918685913})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2797276973724365})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2978483438491821})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3759636878967285})
store['active_learning_steps'][52]['eval_training']['best_epoch']=4
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 32276], ['id', 15223], ['id', 50510], ['id', 6097], ['id', 15823]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9686485680253705, 1.8244499766816615, 2.4152321335147753, 2.7674763472225057, 2.978496557106663]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.4396791458129883})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.7389369010925293})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.7647578716278076})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.084559440612793})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.562140464782715})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.218045473098755})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.7433910369873047})
store['active_learning_steps'][53]['training']['best_epoch']=4
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6658, 'crossentropy': 2.14443203125}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3324984312057495})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.5496366024017334})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3533096313476562})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.347859501838684})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2915546894073486})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3018968105316162})
store['active_learning_steps'][53]['eval_training']['best_epoch']=5
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 36290], ['id', 12745], ['id', 51471], ['id', 40872], ['id', 29329]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.042851653027144, 1.8952619154681256, 2.557336665718214, 2.900743903222798, 3.13543928671705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.60569429397583})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.7776806354522705})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.0736243724823})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.3402047157287598})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.6730432510375977})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.891650438308716})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.848306655883789})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.564943790435791})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.059199810028076})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.286576747894287})
store['active_learning_steps'][54]['training']['best_epoch']=7
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6382, 'crossentropy': 3.053608984375}
