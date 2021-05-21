store = {}
store['timestamp']=1621477581
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=42']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=42
store['worker_id']=42
store['num_workers']=80
store['config']={'seed': 1278, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.4656805992126465})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.7688686847686768})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.1503405570983887})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.01365065574646})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.533437967300415})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.255842685699463})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.0012779235839844})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.2322752475738525})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.030745029449463})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.203981399536133})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.177804470062256})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.286436080932617})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.8202104568481445})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 3.874225616455078})
store['active_learning_steps'][0]['training']['best_epoch']=11
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6715, 'crossentropy': 3.0429732421875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 34678], ['id', 35097], ['id', 48102], ['id', 2061], ['id', 7839]], 'labels': [8, 5, 7, 6, 2], 'scores': [1.3230697492077905, 2.46355497157351, 3.3383244780563235, 3.897204134185696, 4.226471570126067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.2869136333465576})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.290489673614502})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.5242013931274414})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.7724924087524414})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.789827823638916})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.7493505477905273})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.2849202156066895})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6978, 'crossentropy': 2.4341626953125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 41556], ['id', 28371], ['id', 6175], ['id', 1361], ['id', 39513]], 'labels': [0, 3, 3, 2, 5], 'scores': [1.2390363001279243, 2.2889037306122075, 3.1394903049110496, 3.7155956217244785, 4.093581993609212]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.5526854991912842})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.9847387075424194})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.9681837558746338})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.4971909523010254})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.306680679321289})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.2248430252075195})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7524, 'crossentropy': 1.8574583984375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 24408], ['id', 33141], ['id', 49841], ['id', 21648], ['id', 45005]], 'labels': [5, 9, 3, 4, 3], 'scores': [1.2221685327847276, 2.236736352427677, 3.0279751816320495, 3.6286894952980653, 4.027204482956326]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.6517754793167114})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.1021509170532227})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.1802256107330322})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.9945425987243652})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.5756289958953857})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.201810121536255})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.4821786880493164})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7324, 'crossentropy': 1.9782248046875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 52144], ['id', 1364], ['id', 45705], ['id', 3653], ['id', 31885]], 'labels': [2, 9, 2, 9, 4], 'scores': [1.2357847787661855, 2.2745510134525193, 3.108548525789989, 3.6833347642432415, 4.065291374456237]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.446681261062622})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.74521803855896})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.7489784955978394})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.85526442527771})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.0339322090148926})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.9360721111297607})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7451, 'crossentropy': 1.6659525390625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 34758], ['id', 4909], ['id', 42037], ['id', 30286], ['id', 14256]], 'labels': [8, 8, 2, 7, 6], 'scores': [1.1999978972366954, 2.26980896996494, 3.0853810351718716, 3.6644717404470697, 4.034625392465342]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.454747200012207})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.525627613067627})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.679006576538086})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.7570103406906128})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.9269850254058838})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7706, 'crossentropy': 1.4105529296875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 15462], ['id', 52392], ['id', 29634], ['id', 30188], ['id', 8968]], 'labels': [5, 1, 8, 7, 9], 'scores': [1.1649252801236725, 2.148362620625515, 2.967482493893682, 3.5770367590522563, 3.981129359997553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.4841337203979492})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.6216996908187866})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.6864289045333862})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.8962185382843018})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.714982271194458})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 2.0309371948242188})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.9466181993484497})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.7919389009475708})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.785922646522522})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.061598300933838})
store['active_learning_steps'][6]['training']['best_epoch']=7
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7614, 'crossentropy': 1.8665044921875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 42671], ['id', 17389], ['id', 49477], ['id', 58895], ['id', 15510]], 'labels': [2, 3, 3, 4, 2], 'scores': [1.2506179518662879, 2.387405862798418, 3.258923401117811, 3.87093183652466, 4.21761356521084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.2506681680679321})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.4467226266860962})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.4069205522537231})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.4991390705108643})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.7090444564819336})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.6171789169311523})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7974, 'crossentropy': 1.34005390625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 14484], ['id', 14623], ['id', 1239], ['id', 5452], ['id', 48349]], 'labels': [2, 5, 8, 5, 2], 'scores': [1.1202033707497385, 2.123667365441273, 2.9499162282372815, 3.5369692182011647, 3.9599769997425796]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.1571757793426514})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.3757853507995605})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.5336189270019531})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.8088101148605347})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.6140801906585693})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.815606951713562})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.8502397537231445})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.8057533502578735})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8179, 'crossentropy': 1.295519921875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 14385], ['id', 34829], ['id', 23112], ['id', 14749], ['id', 3374]], 'labels': [8, 5, 8, 0, 9], 'scores': [1.1642165547330783, 2.247346255099708, 3.1099163909272054, 3.7142729616746006, 4.109932097127955]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.1895906925201416})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.396856665611267})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.7065868377685547})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.6100820302963257})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.6957192420959473})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.087007522583008})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.9576958417892456})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8096, 'crossentropy': 1.351769921875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 20050], ['id', 56191], ['id', 7437], ['id', 3268], ['id', 51118]], 'labels': [9, 3, 7, 6, 2], 'scores': [1.1278213850131331, 2.1472850647075727, 3.0189067052646, 3.6512503487586976, 4.068305662776865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.2314610481262207})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.2682640552520752})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.35052490234375})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.451909065246582})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.3638112545013428})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.4606730937957764})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.3981550931930542})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.4982647895812988})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.50942063331604})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.3747014999389648})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.532792568206787})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.7621923685073853})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.6214171648025513})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.726660966873169})
store['active_learning_steps'][10]['training']['best_epoch']=11
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.834, 'crossentropy': 1.39769228515625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 28102], ['id', 55743], ['id', 24899], ['id', 52866], ['id', 14722]], 'labels': [0, 3, 3, 7, 0], 'scores': [1.2720565072448102, 2.4145125287790874, 3.298378322905018, 3.9011034576272134, 4.246667440761302]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0868805646896362})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.307753562927246})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2738659381866455})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2521202564239502})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.4557312726974487})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.5646287202835083})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.4618237018585205})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8371, 'crossentropy': 1.1011099609375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 19590], ['id', 47068], ['id', 2574], ['id', 59987], ['id', 57300]], 'labels': [5, 4, 7, 0, 3], 'scores': [1.0911498991756696, 2.101221195238727, 2.887337665253492, 3.5017868440250757, 3.9310413295268507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.058535099029541})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1651434898376465})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0533473491668701})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.099438190460205})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2605544328689575})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.3307435512542725})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2660529613494873})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8517, 'crossentropy': 1.06340693359375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 49354], ['id', 12497], ['id', 53872], ['id', 11087], ['id', 35635]], 'labels': [0, 0, 8, 8, 4], 'scores': [1.1450016193242643, 2.156163908452628, 3.0172620009305167, 3.6235177273601673, 4.02294046319847]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.9753769636154175})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9368536472320557})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9546818733215332})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9446654319763184})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0537388324737549})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0245404243469238})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.154924750328064})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1890804767608643})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1215698719024658})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.87, 'crossentropy': 0.90337021484375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 5600], ['id', 58560], ['id', 22154], ['id', 32880], ['id', 45446]], 'labels': [6, 0, 3, 0, 7], 'scores': [1.1648497183569937, 2.26078934278441, 3.153690612091486, 3.7920909739566397, 4.152234232197914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9807736873626709})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0063621997833252})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1873273849487305})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.153952956199646})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.250154733657837})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8613, 'crossentropy': 0.9191283203125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 28469], ['id', 47260], ['id', 47132], ['id', 23059], ['id', 43782]], 'labels': [5, 6, 2, 1, 3], 'scores': [1.024965827240321, 1.9011949334630938, 2.670489905947207, 3.2707119612989475, 3.7035729293890043]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9479696750640869})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8592618107795715})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9359991550445557})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8944571614265442})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9063035845756531})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9827286005020142})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8557924032211304})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9226558208465576})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0818569660186768})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9235952496528625})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8909, 'crossentropy': 0.79514755859375}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 13096], ['id', 52889], ['id', 3719], ['id', 12476], ['id', 40719]], 'labels': [9, -1, 2, 5, 4], 'scores': [1.1575877182876475, 2.2443400979100874, 3.1646156293140457, 3.7478289416856914, 4.124692234984219]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.956572413444519})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8483041524887085})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8504578471183777})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.160262107849121})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8739931583404541})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8904249668121338})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9307796955108643})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9683992862701416})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8837, 'crossentropy': 0.77480537109375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 24457], ['id', 36818], ['id', 46476], ['id', 15701], ['id', 36704]], 'labels': [8, 7, 5, 3, 2], 'scores': [1.153763352818482, 2.159678920367277, 3.0124358724614844, 3.6057808003767393, 4.0084943023992805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9782752990722656})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8707557916641235})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8840608596801758})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9981812834739685})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9649617671966553})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.3070112466812134})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8693, 'crossentropy': 0.815957275390625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 52959], ['id', 15406], ['id', 13709], ['id', 14650], ['id', 47741]], 'labels': [2, 8, 6, 4, 5], 'scores': [1.0215526724308008, 1.9719151511238016, 2.798461621498001, 3.4281043769225397, 3.8519206147385647]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0659780502319336})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9018464088439941})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9128926396369934})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8174785375595093})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9632006287574768})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8876410126686096})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9368797540664673})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9658229351043701})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0174556970596313})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9537584781646729})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.897, 'crossentropy': 0.792205419921875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 18240], ['id', 7695], ['id', 37219], ['id', 36126], ['id', 6474]], 'labels': [3, 2, 8, 5, 6], 'scores': [1.2833783223982336, 2.3457236862789963, 3.1861553793795956, 3.7780436723752366, 4.162747382298406]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.9678401350975037})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7175594568252563})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7846779823303223})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7588557004928589})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8563255071640015})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8098248243331909})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8624851703643799})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8165462613105774})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.894534707069397})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8179090023040771})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8825953602790833})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9075, 'crossentropy': 0.7306033203125}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 50317], ['id', 37769], ['id', 11569], ['id', 17728], ['id', 45024]], 'labels': [3, 7, 5, 6, 5], 'scores': [1.2660188333922113, 2.3480628688095706, 3.2384614331859662, 3.8567072022696873, 4.221916615473047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8998470306396484})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6769875288009644})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6893026828765869})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.778510570526123})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7706164121627808})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8168894052505493})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.5907396484375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 49537], ['id', 52358], ['id', 45917], ['id', 59314], ['id', 10258]], 'labels': [2, 2, 9, 9, 5], 'scores': [1.0048387442048958, 1.904422144638973, 2.652844256556869, 3.269885090409158, 3.7166003327535844]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8619105815887451})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7067627310752869})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.701949954032898})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6326284408569336})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7326733469963074})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7561275362968445})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7488567233085632})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9191, 'crossentropy': 0.565171728515625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 45047], ['id', 13942], ['id', 59726], ['id', 21880], ['id', 670]], 'labels': [2, 4, 5, 2, 3], 'scores': [1.07583636389659, 2.0544086189350717, 2.8560024498340892, 3.4692352748169846, 3.9029382156964285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9715887308120728})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7017509937286377})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7353549003601074})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6638686656951904})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6950198411941528})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6831754446029663})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6514160633087158})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6605212688446045})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6783175468444824})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7618998289108276})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.929, 'crossentropy': 0.563743994140625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 49487], ['id', 31090], ['id', 26527], ['id', 3810], ['id', 27898]], 'labels': [8, 4, 9, 3, 2], 'scores': [1.1754239911712907, 2.2740693407134143, 3.1349034123944364, 3.7335977869814965, 4.112700031369197]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0304958820343018})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7190067768096924})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6915892362594604})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7543866634368896})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7023671865463257})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7716132402420044})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9133, 'crossentropy': 0.6119240234375}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 42101], ['id', 1674], ['id', 40378], ['id', 59294], ['id', 38760]], 'labels': [5, 9, -1, 8, 9], 'scores': [0.9828019789770805, 1.920596775681414, 2.7178143212207972, 3.320974621588457, 3.7385034418453404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.0598888397216797})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6841558814048767})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6752551198005676})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7360225915908813})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.825645387172699})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9062, 'crossentropy': 0.6236580078125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 14825], ['id', 10181], ['id', 5679], ['id', 4153], ['id', 9118]], 'labels': [3, -1, 3, 2, 9], 'scores': [0.8861843946249366, 1.6872625733233022, 2.393441966562764, 2.979038719716259, 3.4326400516630997]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.026212453842163})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7109991312026978})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6920199990272522})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7337689995765686})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7264131307601929})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8295187950134277})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7734254598617554})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8074522018432617})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9044, 'crossentropy': 0.64150302734375}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 44998], ['id', 22513], ['id', 52228], ['id', 10156], ['id', 18598]], 'labels': [4, 7, 0, 1, 9], 'scores': [1.0525619240952835, 2.0170481649386516, 2.8224726698954097, 3.4716005803073857, 3.910370222197776]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0726397037506104})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6402604579925537})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6197235584259033})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6413156986236572})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6666895151138306})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.658566415309906})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.663772463798523})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6415841579437256})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7123035788536072})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6874947547912598})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7235983610153198})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7993627786636353})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.747657299041748})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7505010962486267})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8079738616943359})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.8297073841094971})
store['active_learning_steps'][26]['training']['best_epoch']=13
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9299, 'crossentropy': 0.614411962890625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 57416], ['id', 1423], ['id', 30322], ['id', 11747], ['id', 52294]], 'labels': [-1, 0, 8, 3, 0], 'scores': [1.1666740640965456, 2.2381293765464063, 3.103144034233818, 3.7381082058997794, 4.136527527221846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.1050018072128296})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5840144157409668})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5896562337875366})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6108428835868835})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6118403673171997})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6784176826477051})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6864817142486572})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5833675861358643})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6972026228904724})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7420598268508911})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.685567319393158})
store['active_learning_steps'][27]['training']['best_epoch']=8
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9351, 'crossentropy': 0.5328173828125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 43575], ['id', 42317], ['id', 57714], ['id', 4822], ['id', 26444]], 'labels': [2, 5, 1, 4, 1], 'scores': [1.1945956029208158, 2.242369404207703, 3.125904710553444, 3.7468009568681246, 4.1228326135163895]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.1325623989105225})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6604509949684143})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6214043498039246})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6875611543655396})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7153030633926392})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.670452356338501})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.567624568939209})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6596512794494629})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6547113656997681})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6740304231643677})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.737950325012207})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9302, 'crossentropy': 0.5581728515625}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 42415], ['id', 2835], ['id', 10450], ['id', 26184], ['id', 2803]], 'labels': [7, -1, 3, 0, 3], 'scores': [1.1792156631332524, 2.2392777081771804, 3.1117465630400734, 3.768411509384464, 4.148885970535308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.049513339996338})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6477550268173218})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.609096884727478})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5983281135559082})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6079981327056885})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6393762826919556})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6391274929046631})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9279, 'crossentropy': 0.5351150390625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 1642], ['id', 29376], ['id', 51155], ['id', 54858], ['id', 17494]], 'labels': [6, -1, 4, 3, 5], 'scores': [0.9716422300350138, 1.8875479009098388, 2.6746337032681087, 3.329525435481248, 3.794835816846744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.077268362045288})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6620693206787109})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5399409532546997})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6425225734710693})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6638633012771606})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6347532272338867})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9356, 'crossentropy': 0.473468310546875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 41453], ['id', 49616], ['id', 32427], ['id', 51432], ['id', 32445]], 'labels': [3, 7, 0, 1, 5], 'scores': [0.923149374613141, 1.7612969977286204, 2.5164950221895754, 3.1207249314446193, 3.5825369455587577]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.0823309421539307})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6888933181762695})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6719647645950317})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7016422748565674})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6575555801391602})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5903383493423462})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7531416416168213})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6913032531738281})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8447412848472595})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7412526607513428})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7766836881637573})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9279, 'crossentropy': 0.60569287109375}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 35401], ['id', 41002], ['id', 3251], ['id', 622], ['id', 5443]], 'labels': [3, 7, 8, 5, -1], 'scores': [1.0929343000034062, 2.081657069964768, 2.955984183580733, 3.6174579782511174, 4.046549910840912]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.2158992290496826})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6631836891174316})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5731508731842041})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5411485433578491})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5754651427268982})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6291050910949707})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6390042304992676})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6343082189559937})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9343, 'crossentropy': 0.506058203125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 18845], ['id', 20037], ['id', 9390], ['id', 4646], ['id', 41295]], 'labels': [2, 8, 9, 2, 9], 'scores': [1.102167965770119, 2.010706070952291, 2.7738259617308287, 3.3664601716492424, 3.803548640531405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.2485615015029907})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6732245683670044})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.538357138633728})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5423094034194946})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5539366006851196})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5620675683021545})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.529568076133728})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6292458176612854})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6162582039833069})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5764834880828857})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9362, 'crossentropy': 0.4876775390625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 58961], ['id', 28512], ['id', 517], ['id', 50736], ['id', 16756]], 'labels': [9, 5, 8, -1, 7], 'scores': [1.0972851007104418, 2.0725776099984596, 2.8749958942090466, 3.496111601966013, 3.93091761056856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.1595852375030518})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6390573978424072})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5280759930610657})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5535537004470825})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6783691644668579})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5972628593444824})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9396, 'crossentropy': 0.494443701171875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 34946], ['id', 12254], ['id', 18324], ['id', 39172], ['id', 17941]], 'labels': [8, 2, 0, 9, 0], 'scores': [0.8839844345870658, 1.7132208115614134, 2.435349531921098, 3.031264062867212, 3.4928778754602803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0173044204711914})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5408897995948792})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.47315651178359985})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5014214515686035})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4943618178367615})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5068647265434265})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5488575100898743})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9416, 'crossentropy': 0.4426578125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 30884], ['id', 5536], ['id', 50736], ['id', 40654], ['id', 20170]], 'labels': [2, 8, -1, 5, 9], 'scores': [1.0673547514453503, 1.9759518091724892, 2.7147469257588295, 3.314343814233373, 3.750212437691239]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1979241371154785})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6716564893722534})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5504754185676575})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5735193490982056})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.559686541557312})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6015511751174927})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6323909759521484})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5707611441612244})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9445, 'crossentropy': 0.456566357421875}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 13969], ['id', 27458], ['id', 57474], ['id', 41933], ['id', 16488]], 'labels': [3, 2, 3, 5, 9], 'scores': [0.9891892026800848, 1.8967317463936744, 2.685273469664015, 3.3020516994506277, 3.7465302855721143]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.2655988931655884})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6541483402252197})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6541458368301392})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5864112973213196})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5747461915016174})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6082767248153687})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.563518762588501})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5782566666603088})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9367, 'crossentropy': 0.48991796875}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 26266], ['id', 48006], ['id', 1814], ['id', 52086], ['id', 21150]], 'labels': [7, 6, 4, 5, 3], 'scores': [1.0415102421927767, 1.9563078590225969, 2.73373249994736, 3.3405537289690717, 3.7764596035210793]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.177147626876831})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7045191526412964})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5322021245956421})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.513786792755127})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5010983347892761})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47047099471092224})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.498818963766098})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5954754948616028})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5017977952957153})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5160326957702637})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4948714077472687})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5364441871643066})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.506285548210144})
store['active_learning_steps'][38]['training']['best_epoch']=10
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9478, 'crossentropy': 0.4594810546875}
