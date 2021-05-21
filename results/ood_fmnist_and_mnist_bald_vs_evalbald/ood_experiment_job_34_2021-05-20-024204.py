store = {}
store['timestamp']=1621474924
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=34']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=34
store['worker_id']=34
store['num_workers']=80
store['config']={'seed': 1270, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.9167261123657227})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.3811326026916504})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.3278021812438965})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.0156688690185547})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7158, 'crossentropy': 1.8141203125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3452866077423096})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3396470546722412})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.3145701885223389})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 6027], ['id', 5596], ['id', 16033], ['id', 22041], ['id', 7372]], 'labels': [5, 7, 2, 9, -1], 'scores': [0.9443897225288551, 1.6226526906366434, 2.1002019523688, 2.4549532190470265, 2.700993118999005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.190721035003662})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.5396780967712402})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.725980281829834})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.0468363761901855})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.1771843433380127})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.0538716316223145})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6938, 'crossentropy': 2.2669662109375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.4094301462173462})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.6952133178710938})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.6455470323562622})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.7330878973007202})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 37946], ['id', 30738], ['id', 20270], ['id', 48324], ['id', 13653]], 'labels': [0, 8, -1, 3, -1], 'scores': [0.7552434759738353, 1.4095956407654153, 1.8533561318943113, 2.152609516921851, 2.3371417770142617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.15610408782959})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.349423408508301})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.4073896408081055})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.6033029556274414})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.8072669506073})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7215, 'crossentropy': 2.1181880859375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.3213629722595215})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.2964708805084229})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.2910571098327637})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.314372181892395})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 36894], ['id', 23391], ['id', 48271], ['id', 22991], ['id', 21147]], 'labels': [0, 8, 7, 4, 2], 'scores': [0.8992521131380142, 1.630171950840087, 2.1986473216778846, 2.605984043369273, 2.892739466910837]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.349642276763916})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.676828384399414})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.77445387840271})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.7509610652923584})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7703, 'crossentropy': 1.2545119140625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.1361544132232666})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.0458735227584839})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 0.9834858775138855})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 33357], ['id', 32022], ['id', 12957], ['id', 8794], ['id', 8926]], 'labels': [3, 2, 5, 3, 0], 'scores': [0.7694203622053088, 1.4252278906643352, 1.930902134388223, 2.2938154504234083, 2.5387075737482405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.516546368598938})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.6245577335357666})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.8105971813201904})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.016871452331543})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.9183558225631714})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.2337846755981445})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.3853042125701904})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.694808006286621})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.4757189750671387})
store['active_learning_steps'][4]['training']['best_epoch']=6
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7776, 'crossentropy': 1.8152353515625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.383662223815918})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.3950302600860596})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.2989140748977661})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.3281781673431396})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.215982437133789})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.3484705686569214})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.2351406812667847})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 8200], ['id', 41147], ['id', 58445], ['id', 6997], ['id', 24221]], 'labels': [3, 5, 8, 5, 7], 'scores': [0.8763653313078539, 1.623732254122734, 2.200427235203384, 2.559889799841107, 2.804035829609443]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.5704495906829834})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.897512435913086})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.8714346885681152})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 2.1463565826416016})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 2.124168634414673})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 2.030308485031128})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 2.1620726585388184})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 2.3782119750976562})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 2.3538365364074707})
store['active_learning_steps'][5]['training']['best_epoch']=6
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7811, 'crossentropy': 1.8321654296875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.3362716436386108})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.2609951496124268})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.1855971813201904})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2399895191192627})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.1563239097595215})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.2041923999786377})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.1738017797470093})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 22442], ['id', 12650], ['id', 44121], ['id', 27096], ['id', 5842]], 'labels': [2, 5, 0, 8, 1], 'scores': [0.8091841520969411, 1.4790341032836283, 2.017493131974508, 2.355513214148343, 2.576806821107483]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.4399381875991821})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.7420613765716553})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.7769193649291992})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.1075189113616943})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.176419734954834})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 2.1407766342163086})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7862, 'crossentropy': 1.54455966796875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.3465220928192139})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.2498927116394043})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.1884427070617676})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.186630129814148})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.2027003765106201})
store['active_learning_steps'][6]['eval_training']['best_epoch']=5
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 48643], ['id', 11843], ['id', 17572], ['id', 59502], ['id', 26863]], 'labels': [2, 8, 5, 5, 2], 'scores': [0.7893518438643026, 1.433420972520617, 1.9518740281567348, 2.297170420132205, 2.527136029918416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.4453015327453613})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.578694224357605})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.736426830291748})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.921344518661499})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.870039463043213})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8006, 'crossentropy': 1.365505078125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.2034382820129395})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.1420931816101074})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.0419570207595825})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.0217459201812744})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 13931], ['id', 14733], ['id', 45101], ['id', 45761], ['id', 25765]], 'labels': [3, 8, 5, 4, 5], 'scores': [0.8772923618419315, 1.5260061927708382, 2.0481414439302896, 2.3984154315353052, 2.6255056328022395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.4198319911956787})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.5090856552124023})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.6285145282745361})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.6621601581573486})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.7507503032684326})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.6996848583221436})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 2.029064178466797})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.8458778858184814})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.7887643575668335})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.9377657175064087})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.8493571281433105})
store['active_learning_steps'][8]['training']['best_epoch']=8
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8279, 'crossentropy': 1.5157345703125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.2488000392913818})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.239100694656372})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.2537672519683838})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.2454698085784912})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2684556245803833})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.1895769834518433})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.1254611015319824})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.207343578338623})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.1871691942214966})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.242673397064209})
store['active_learning_steps'][8]['eval_training']['best_epoch']=7
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 28838], ['id', 15216], ['id', 1302], ['id', 5580], ['id', 23718]], 'labels': [9, 3, 7, 4, 2], 'scores': [0.7877004611009852, 1.4221454019974629, 1.9665463819014004, 2.3331246044209966, 2.592699683573633]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.2700986862182617})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.5441100597381592})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.6327850818634033})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.787620186805725})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.8231161832809448})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.7243702411651611})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8082, 'crossentropy': 1.46801455078125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.26722252368927})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.1863601207733154})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.171075701713562})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.1128816604614258})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.1165345907211304})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 16922], ['id', 59368], ['id', 27374], ['id', 15505], ['id', 7798]], 'labels': [3, 5, 2, 0, 9], 'scores': [0.6989414622958849, 1.31400413447341, 1.8350391927612084, 2.2465975757766463, 2.5372112915237244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.278913140296936})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.422054409980774})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.819523572921753})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.8842973709106445})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 2.0571491718292236})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7971, 'crossentropy': 1.31452470703125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.284698724746704})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.0855913162231445})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.0414279699325562})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.0888490676879883})
store['active_learning_steps'][10]['eval_training']['best_epoch']=2
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 51722], ['id', 20113], ['id', 29530], ['id', 50202], ['id', 44443]], 'labels': [4, 6, 4, 5, -1], 'scores': [0.6802668992433518, 1.2831582700117234, 1.7757582880459304, 2.1332678043490496, 2.3692263616477955]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.196997880935669})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.468761920928955})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.6062194108963013})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.7078514099121094})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.7439395189285278})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.9242182970046997})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.8627192974090576})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.8612251281738281})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.7569200992584229})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.947263479232788})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.8424780368804932})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 2.039663314819336})
store['active_learning_steps'][11]['training']['best_epoch']=9
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8264, 'crossentropy': 1.52926708984375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.1118271350860596})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.2460970878601074})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0517083406448364})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.1486055850982666})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.1262462139129639})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.162868618965149})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.1444580554962158})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.053741216659546})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 44425], ['id', 24708], ['id', 14972], ['id', 41489], ['id', 18404]], 'labels': [2, 5, 4, 2, 5], 'scores': [0.8423126022946397, 1.487597894687048, 2.0250249077933042, 2.3847458479960717, 2.610440698075078]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.292707085609436})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.4701592922210693})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.4849188327789307})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.7333524227142334})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.8103331327438354})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.975844383239746})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.7265868186950684})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.8689206838607788})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 2.276726722717285})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.912168264389038})
store['active_learning_steps'][12]['training']['best_epoch']=7
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8194, 'crossentropy': 1.472552734375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.109236478805542})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.2409820556640625})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.067356824874878})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.1166778802871704})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.1579090356826782})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.0287208557128906})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0079525709152222})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 49212], ['id', 5247], ['id', 55898], ['id', 52356], ['id', 28181]], 'labels': [7, 2, 4, 9, 8], 'scores': [0.8806734034412481, 1.6379919546778963, 2.224740142565598, 2.661486292138317, 2.960314454427283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0425868034362793})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.2192203998565674})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.3993496894836426})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.3590713739395142})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.4734861850738525})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.6776747703552246})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.6700674295425415})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.456085205078125})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.7255399227142334})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.772939682006836})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.7324193716049194})
store['active_learning_steps'][13]['training']['best_epoch']=8
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8388, 'crossentropy': 1.28829296875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0922749042510986})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.1418989896774292})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.038769245147705})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.092024803161621})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0556058883666992})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9363075494766235})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.957981288433075})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9770349860191345})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9257129430770874})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9738827347755432})
store['active_learning_steps'][13]['eval_training']['best_epoch']=9
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 56472], ['id', 29312], ['id', 19190], ['id', 10073], ['id', 13114]], 'labels': [7, 2, 9, 2, 3], 'scores': [0.8337947896326954, 1.5351326471214524, 2.1049038837205662, 2.460409426355419, 2.683074527564262]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.0627721548080444})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1715857982635498})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.4043841361999512})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2973315715789795})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.7326207160949707})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.6773549318313599})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.7709704637527466})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8307, 'crossentropy': 1.15964638671875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0282509326934814})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0110108852386475})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.0203893184661865})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.982797384262085})
store['active_learning_steps'][14]['eval_training']['best_epoch']=1
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 10744], ['id', 36529], ['id', 8680], ['id', 36128], ['id', 27449]], 'labels': [7, 8, 8, -1, -1], 'scores': [0.6497267933223063, 1.2354886977002169, 1.6963562855403698, 1.9838421228878236, 2.1525814526785716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.063061237335205})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.2826513051986694})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.4371365308761597})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.418103575706482})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.7828214168548584})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.6535224914550781})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8355, 'crossentropy': 1.19845517578125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.0654380321502686})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0026237964630127})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9673292636871338})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9205012321472168})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9551060199737549})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 30996], ['id', 54004], ['id', 56457], ['id', 46045], ['id', 36329]], 'labels': [1, 0, 3, 6, -1], 'scores': [0.6446182422418736, 1.1531300858011861, 1.5794925057129081, 1.8970716869585083, 2.077889768498979]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.1380516290664673})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.20267915725708})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2747163772583008})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.4857778549194336})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.39667809009552})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.5967289209365845})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8555, 'crossentropy': 0.97735478515625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0278724431991577})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8606306314468384})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.824883222579956})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.805392324924469})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7998735308647156})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 34122], ['id', 33383], ['id', 48072], ['id', 26546], ['id', 17804]], 'labels': [5, 1, 9, 4, 8], 'scores': [0.672527477199359, 1.2619450216787111, 1.7456827471356764, 2.132577081322239, 2.3845331240720817]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9391392469406128})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9807108640670776})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9155205488204956})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0225346088409424})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1939890384674072})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.287175178527832})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.2284271717071533})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8814, 'crossentropy': 0.84470859375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9789734482765198})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8878160715103149})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8147107362747192})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8644927740097046})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7716909646987915})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7593361735343933})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 10315], ['id', 49607], ['id', 6044], ['id', 49824], ['id', 55233]], 'labels': [7, 3, 2, 8, 5], 'scores': [0.658474344509103, 1.2290411585051144, 1.6770542067146197, 1.9450594125390115, 2.1249203752789487]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9689476490020752})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8629355430603027})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.038306713104248})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0265703201293945})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.168184757232666})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8861, 'crossentropy': 0.71443203125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.946521520614624})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7354007959365845})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6739819049835205})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6867450475692749})
store['active_learning_steps'][18]['eval_training']['best_epoch']=3
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 34847], ['id', 42193], ['id', 51845], ['id', 3748], ['id', 16795]], 'labels': [0, 5, 0, 2, 7], 'scores': [0.5681918130100552, 1.0690070963769984, 1.4874380434867445, 1.8191615206809484, 2.0517559423525675]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9745392799377441})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9106127619743347})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9963452219963074})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0547540187835693})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.1392741203308105})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.2475812435150146})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.2684574127197266})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.1964826583862305})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.3542039394378662})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.3497520685195923})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.2888414859771729})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.3725183010101318})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.400296688079834})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.355670690536499})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.6440128087997437})
store['active_learning_steps'][19]['training']['best_epoch']=12
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8831, 'crossentropy': 1.0820228515625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9441746473312378})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9094513654708862})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7735202312469482})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8453269600868225})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7796465158462524})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7857824563980103})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.836952269077301})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8108686804771423})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8377406597137451})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7739812731742859})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7627730369567871})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7652497291564941})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7235493659973145})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7184997797012329})
store['active_learning_steps'][19]['eval_training']['best_epoch']=12
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 14367], ['id', 20726], ['id', 19168], ['id', 58560], ['id', 30742]], 'labels': [3, 4, 1, 0, 1], 'scores': [0.8475573365095899, 1.5839991229155197, 2.190498561333679, 2.6374033336062763, 2.875381767455184]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8994119167327881})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9485570192337036})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.2501850128173828})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9318843483924866})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.118788480758667})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.1590092182159424})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.153611421585083})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8897, 'crossentropy': 0.777279443359375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.1070451736450195})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8611679673194885})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8260643482208252})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.743630051612854})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7550888061523438})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7664694786071777})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 59314], ['id', 38932], ['id', 826], ['id', 36783], ['id', 36072]], 'labels': [9, 5, 9, 0, 2], 'scores': [0.6875703373023276, 1.3153185424468075, 1.8340528452062403, 2.1965865941538514, 2.4149457307446625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9230153560638428})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0164486169815063})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0081567764282227})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0352286100387573})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.1400814056396484})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.2094395160675049})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.303090214729309})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.222597599029541})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8878, 'crossentropy': 0.8652251953125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0145190954208374})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9299524426460266})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8246596455574036})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7790836095809937})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7892106771469116})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7497900724411011})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.712806224822998})
store['active_learning_steps'][21]['eval_training']['best_epoch']=7
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 43031], ['id', 11871], ['id', 44853], ['id', 659], ['id', 20093]], 'labels': [3, 6, 7, 3, 5], 'scores': [0.7613283025878431, 1.3431632662557882, 1.8245164347704397, 2.1831410952459436, 2.4234112129981185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.8930339813232422})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6769704818725586})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7691196203231812})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7571929693222046})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8456714749336243})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9133, 'crossentropy': 0.5888263671875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8470225930213928})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6195247173309326})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.602985143661499})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.520971417427063})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 59783], ['id', 26733], ['id', 5155], ['id', 1143], ['id', 56726]], 'labels': [1, 2, 4, 2, 9], 'scores': [0.677169786682166, 1.2790057978930047, 1.734015990293126, 2.0713024113870686, 2.2772090298279277]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8774642944335938})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6817355155944824})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6415481567382812})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.758263349533081})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7668060064315796})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7905104756355286})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.533548876953125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8894545435905457})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6134872436523438})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5919162631034851})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5690441131591797})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5440680384635925})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 20869], ['id', 26034], ['id', 33046], ['id', 35802], ['id', 28412]], 'labels': [3, 5, 5, -1, 0], 'scores': [0.7029653933576602, 1.2830210367118529, 1.7172022740429442, 2.0536986656200558, 2.2878395319631277]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8359991312026978})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.703251302242279})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6519613862037659})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7016856670379639})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.659600555896759})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7447450160980225})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9229, 'crossentropy': 0.53221728515625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9320840835571289})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6653481721878052})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5688556432723999})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5284298658370972})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5489769577980042})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 5474], ['id', 2369], ['id', 50576], ['id', 39877], ['id', 45622]], 'labels': [8, -1, 2, 7, 6], 'scores': [0.6890815737621498, 1.259501799131785, 1.6823943721791137, 1.959170169978524, 2.1217325394967137]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9481970071792603})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.742682933807373})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7601491212844849})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7142307758331299})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8596611022949219})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7867399454116821})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7461221814155579})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.938815176486969})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9071295261383057})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9112685918807983})
store['active_learning_steps'][25]['training']['best_epoch']=7
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9147, 'crossentropy': 0.6119306640625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.0733145475387573})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6147688627243042})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5636814832687378})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5377249121665955})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5604496598243713})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5093607902526855})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5090869665145874})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 52981], ['id', 10736], ['id', 39314], ['id', 16286], ['id', 13460]], 'labels': [5, 4, -1, 0, 5], 'scores': [0.7060827795360818, 1.3280556302621278, 1.8344929528321714, 2.249229088604431, 2.4909280857655887]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9654856324195862})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7574480772018433})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.726195216178894})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8233684301376343})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8024228811264038})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8646950721740723})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8987, 'crossentropy': 0.61702705078125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.9714897871017456})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6330680847167969})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5916717648506165})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6109710335731506})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5644016265869141})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 49582], ['id', 31014], ['id', 17222], ['id', 28218], ['id', 42417]], 'labels': [2, 8, 8, -1, 8], 'scores': [0.6099518973470772, 1.1512931225275187, 1.6004848310579805, 1.9387800429831312, 2.166575171461133]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9699511528015137})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.666081428527832})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7024569511413574})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6810221076011658})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7664008140563965})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7727196216583252})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7882305979728699})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9138, 'crossentropy': 0.613306787109375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8658549785614014})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6548786163330078})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6056727170944214})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5037841200828552})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5433576703071594})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.493611216545105})
store['active_learning_steps'][27]['eval_training']['best_epoch']=4
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 14423], ['id', 53215], ['id', 47870], ['id', 48253], ['id', 52513]], 'labels': [6, -1, 9, -1, -1], 'scores': [0.7347568993491096, 1.3404409236088295, 1.8494955744035027, 2.1891890723474097, 2.394942252881469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9091472029685974})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6621822118759155})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6975131034851074})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7703440189361572})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.656895637512207})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8475926518440247})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7389497756958008})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7534010410308838})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9203, 'crossentropy': 0.56842255859375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8670613169670105})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5648753046989441})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4857642650604248})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5066766738891602})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.46994757652282715})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.45725417137145996})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5117177963256836})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 43126], ['id', 57882], ['id', 12000], ['id', 16590], ['id', 59234]], 'labels': [3, 0, 7, 6, -1], 'scores': [0.6466350219529791, 1.2499569476245016, 1.7503374365615807, 2.102220500699028, 2.331656562006085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8575679063796997})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6052963733673096})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5428667068481445})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5727958679199219})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6593223214149475})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.589264988899231})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7721767425537109})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9247, 'crossentropy': 0.51911435546875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8699361085891724})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6305224895477295})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5696497559547424})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5003964304924011})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4899982213973999})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.476998507976532})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 20169], ['id', 12514], ['id', 27838], ['id', 25905], ['id', 41618]], 'labels': [4, 2, 3, -1, 5], 'scores': [0.6578212545776772, 1.2439978719091456, 1.6859703518037499, 2.0043396033121104, 2.21988579991206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1172475814819336})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6503108739852905})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5792635679244995})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6322615146636963})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7343084216117859})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7456360459327698})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7570067048072815})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.914, 'crossentropy': 0.587453271484375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8983184099197388})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6022945642471313})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5375601053237915})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5446460247039795})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5061795711517334})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5104798674583435})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 27183], ['id', 39293], ['id', 41299], ['id', 23434], ['id', 1114]], 'labels': [3, 9, 3, 5, 7], 'scores': [0.6578492537256786, 1.2247616570528823, 1.6696128473238048, 2.012628006890318, 2.2570769837048417]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9755628108978271})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6397968530654907})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5965799689292908})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6307336091995239})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5772706270217896})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5558100938796997})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7054102420806885})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5938773155212402})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6297500729560852})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9303, 'crossentropy': 0.517041748046875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.928012490272522})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6372728943824768})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5605279207229614})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5164571404457092})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5016238689422607})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.49022936820983887})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4577045142650604})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4213498830795288})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 15767], ['id', 8765], ['id', 25661], ['id', 28766], ['id', 4360]], 'labels': [5, 3, 8, -1, 6], 'scores': [0.6238884607773032, 1.1989271563468336, 1.6278584181398, 1.9453034106869245, 2.152992189788475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9024963974952698})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.725427508354187})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6417282223701477})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6219240427017212})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.717759370803833})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7050269246101379})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.565726708984375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9758321046829224})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6140727996826172})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5641488432884216})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5279176831245422})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4992715120315552})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 26358], ['id', 55314], ['id', 50180], ['id', 49354], ['id', 8674]], 'labels': [3, 6, 8, 0, 9], 'scores': [0.6212518046038247, 1.1658219385336865, 1.623321427134906, 1.9368692828949277, 2.1462043260156998]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0028420686721802})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6535162925720215})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5704336762428284})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5987572073936462})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6326426267623901})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6174197196960449})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7537477016448975})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7511014342308044})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6989723443984985})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6528815031051636})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.7305757403373718})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7654186487197876})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.7036384344100952})
store['active_learning_steps'][33]['training']['best_epoch']=10
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9285, 'crossentropy': 0.573733447265625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8705750703811646})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.555884599685669})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5129242539405823})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5017975568771362})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5130360126495361})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.46673446893692017})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4436091184616089})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.43061956763267517})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.44577455520629883})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.403786838054657})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 36417], ['id', 45901], ['id', 59934], ['id', 35860], ['id', 37089]], 'labels': [6, 7, 0, 7, 5], 'scores': [0.7101017894435031, 1.3585000858639964, 1.8819700044515635, 2.255886782556119, 2.529852326082474]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9343117475509644})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6865733861923218})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6119272112846375})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6258630752563477})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6153976917266846})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6444569826126099})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6643091440200806})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6893729567527771})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7104188203811646})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9231, 'crossentropy': 0.56599423828125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8185464143753052})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5838955640792847})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5365791320800781})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4649156928062439})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.46882206201553345})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.434567391872406})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.42756420373916626})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4073145091533661})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 27359], ['id', 39482], ['id', 49890], ['id', 1559], ['id', 9417]], 'labels': [8, 5, 5, 3, -1], 'scores': [0.7414248842053368, 1.4275891562768548, 1.9615332555074834, 2.328490429698375, 2.5678955666941707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0295830965042114})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7463699579238892})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6538369655609131})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.726195216178894})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6319605708122253})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6426136493682861})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.7086887359619141})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6780694127082825})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.7314305305480957})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.687694251537323})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7972151041030884})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.924, 'crossentropy': 0.566612060546875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0882686376571655})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6051137447357178})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5397209525108337})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5336557030677795})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4624101221561432})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4782702922821045})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.44272103905677795})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4557546079158783})
store['active_learning_steps'][35]['eval_training']['best_epoch']=5
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 26444], ['id', 53585], ['id', 43942], ['id', 28362], ['id', 1212]], 'labels': [1, 2, 3, 7, 4], 'scores': [0.8782506343358436, 1.5987848672661165, 2.0977902857320387, 2.4305442638905133, 2.6112285027981823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.0204311609268188})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5853431224822998})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5531185865402222})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5297647714614868})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5628303289413452})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5855835676193237})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.680479884147644})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9313, 'crossentropy': 0.479708935546875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.024813175201416})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6558982133865356})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.534990668296814})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5027178525924683})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5217952728271484})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5000536441802979})
store['active_learning_steps'][36]['eval_training']['best_epoch']=4
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 35830], ['id', 11600], ['id', 52462], ['id', 33596], ['id', 39314]], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.6138453159168393, 1.1699336255444899, 1.6345302288783214, 1.9758700970330265, 2.2176615885631517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.013906717300415})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.568210244178772})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5600500702857971})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5524555444717407})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5998290777206421})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5521042346954346})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6572428941726685})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6386741399765015})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6400927305221558})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9368, 'crossentropy': 0.473269140625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9872751235961914})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6139603853225708})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5283215641975403})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.48455914855003357})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.44695448875427246})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4224560260772705})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4304279088973999})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4287790060043335})
store['active_learning_steps'][37]['eval_training']['best_epoch']=8
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 15779], ['id', 29367], ['id', 36008], ['id', 38760], ['id', 47503]], 'labels': [0, -1, 8, 9, 5], 'scores': [0.7155558962698165, 1.3459391617935057, 1.842974304275172, 2.1881197080571786, 2.406491071794642]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.905550479888916})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5933751463890076})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49282777309417725})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5671041011810303})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49851804971694946})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6085769534111023})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.619076132774353})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5882055759429932})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9347, 'crossentropy': 0.45356103515625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9690459966659546})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6106777191162109})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.48081475496292114})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.48532038927078247})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.47708308696746826})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4209896922111511})
store['active_learning_steps'][38]['eval_training']['best_epoch']=3
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 39314], ['id', 50276], ['id', 6506], ['id', 37549], ['id', 51146]], 'labels': [-1, -1, 8, -1, -1], 'scores': [0.5302246236694614, 1.004580541806415, 1.4308608521198298, 1.7590435745987705, 1.9790050484951207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9838777184486389})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6467409133911133})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5689501762390137})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5821543335914612})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5974542498588562})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6454898715019226})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6134089231491089})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6101356744766235})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6023068428039551})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.7111363410949707})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6812564730644226})
store['active_learning_steps'][39]['training']['best_epoch']=8
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9364, 'crossentropy': 0.512155712890625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0150201320648193})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5916472673416138})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5794302225112915})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.528372049331665})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.46888160705566406})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.43610066175460815})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4512855112552643})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4607768952846527})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4081416130065918})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4199191927909851})
store['active_learning_steps'][39]['eval_training']['best_epoch']=9
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 44753], ['id', 15852], ['id', 26482], ['id', 52192], ['id', 31946]], 'labels': [5, -1, 6, -1, 5], 'scores': [0.6982862565189136, 1.3035508278818502, 1.802144595176829, 2.169920298602441, 2.3906753422123277]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0160002708435059})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.585137128829956})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5564039945602417})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5086122751235962})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5828707218170166})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5596653819084167})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.614022970199585})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6251118183135986})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9297, 'crossentropy': 0.51402021484375}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9866719245910645})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5991100072860718})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.529573917388916})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.47153833508491516})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4979207515716553})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4781308174133301})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4659923315048218})
store['active_learning_steps'][40]['eval_training']['best_epoch']=6
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 36889], ['id', 31413], ['id', 47387], ['id', 5035], ['id', 59466]], 'labels': [7, 5, 8, 7, 8], 'scores': [0.6232177471380715, 1.1975906717416747, 1.6695504368920524, 1.9729752579165822, 2.1801774055480987]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9640820026397705})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.627435028553009})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5604547262191772})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5319321155548096})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5988930463790894})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6623091101646423})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5630122423171997})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9373, 'crossentropy': 0.445367529296875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0019322633743286})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5522692203521729})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5346087217330933})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4542540907859802})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4441990554332733})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.46652114391326904})
store['active_learning_steps'][41]['eval_training']['best_epoch']=5
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 55188], ['id', 30861], ['id', 24134], ['id', 31608], ['id', 1421]], 'labels': [2, 4, 8, 2, 9], 'scores': [0.6534164517647465, 1.2187046672032995, 1.6742841221820974, 2.043946178309402, 2.2976878124427245]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0357158184051514})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5458179116249084})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.47926390171051025})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48324939608573914})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5587483048439026})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5066051483154297})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9417, 'crossentropy': 0.42487841796875}
