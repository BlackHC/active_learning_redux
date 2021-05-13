store = {}
store['timestamp']=1620259228
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=17']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=17
store['worker_id']=17
store['num_workers']=40
store['config']={'seed': 21, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.227459192276001})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.048830509185791})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.0878915786743164})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.1286065578460693})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6614, 'crossentropy': 2.06256171875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 32349], ['id', 2775], ['id', 7635], ['id', 13987], ['id', 12170], ['id', 20882], ['id', 11731], ['ood', 6618], ['id', 15798], ['id', 25355]], 'labels': [8, 5, 3, 4, 6, 2, 6, 9, 0, 7], 'scores': [0.9678052663803101, 0.6264369487762451, 0.678067147731781, 0.618881344795227, 0.7579969763755798, 0.762199342250824, 0.9315457344055176, 0.7555665969848633, 1.102810561656952, 0.6832333207130432]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.4218358993530273})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.636807918548584})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.785412311553955})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 2.1969316005706787})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7825, 'crossentropy': 1.26979189453125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 12196], ['id', 18600], ['id', 17641], ['id', 28780], ['ood', 57221], ['id', 50449], ['id', 41215], ['id', 46325], ['id', 55442], ['id', 37435]], 'labels': [2, 5, 8, 2, 5, 2, 5, 4, 5, 2], 'scores': [0.7421401143074036, 0.6842005252838135, 0.5127471685409546, 0.845637857913971, 0.593235969543457, 0.8703396916389465, 0.7713942527770996, 0.6679519414901733, 0.8010982871055603, 0.8015376329421997]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.3592236042022705})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.5123075246810913})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.7211500406265259})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.8240156173706055})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.775, 'crossentropy': 1.20870302734375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 7436], ['id', 57806], ['id', 45114], ['id', 56479], ['id', 20966], ['id', 53309], ['id', 50116], ['id', 27125], ['id', 21165], ['ood', 53386]], 'labels': [8, 3, 7, 5, 8, 5, 8, 4, 9, 9], 'scores': [0.787156343460083, 0.6232503652572632, 0.7318076491355896, 0.625801682472229, 0.6246501207351685, 0.8564587235450745, 0.6800073385238647, 0.7711285948753357, 0.6660842299461365, 0.3015788793563843]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9755983948707581})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2962838411331177})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.4549039602279663})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.575296401977539})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8071, 'crossentropy': 0.98979423828125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 35656], ['id', 59404], ['id', 1688], ['id', 22953], ['id', 57542], ['id', 20982], ['id', 14844], ['id', 29002], ['id', 28455], ['id', 23011]], 'labels': [4, 9, 6, 6, 0, 9, 9, 7, 5, 5], 'scores': [0.4537796378135681, 0.6940726041793823, 0.5716302394866943, 0.47899329662323, 0.6982266902923584, 0.717482328414917, 0.7621794939041138, 0.5376213788986206, 0.46861910820007324, 0.4614901542663574]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.0866895914077759})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.175528883934021})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.3545582294464111})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.298701286315918})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7817, 'crossentropy': 0.97054169921875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 20509], ['id', 57632], ['id', 1317], ['id', 4935], ['id', 24038], ['id', 27131], ['id', 47723], ['id', 7865], ['id', 2127], ['id', 36338]], 'labels': [7, 2, 3, 2, 1, 2, 8, 5, 3, 3], 'scores': [0.49438923597335815, 0.6201677322387695, 0.6072725057601929, 0.5696804523468018, 0.7320065498352051, 0.6639122366905212, 0.7041578888893127, 0.6114291548728943, 0.5583237409591675, 0.41688621044158936]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.020777702331543})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.115187406539917})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.324394941329956})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.5014992952346802})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8094, 'crossentropy': 0.933293359375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 5981], ['id', 48098], ['id', 23315], ['id', 42990], ['id', 50054], ['id', 11346], ['id', 48653], ['id', 12653], ['id', 45761], ['id', 23305]], 'labels': [0, 7, 0, 8, 8, 2, 4, 0, 4, 0], 'scores': [0.5966318249702454, 0.691993772983551, 0.7884435653686523, 0.653093159198761, 0.5898518562316895, 0.5987616777420044, 0.6080321073532104, 0.7086787819862366, 0.5176104307174683, 0.7029843926429749]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8986150026321411})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9590774774551392})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.962802529335022})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0376157760620117})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8417, 'crossentropy': 0.805705712890625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 59446], ['id', 6618], ['id', 52939], ['id', 22779], ['id', 34610], ['id', 50017], ['id', 20790], ['id', 52478], ['id', 35613], ['id', 11887]], 'labels': [5, 8, 3, 5, 5, 5, 3, 9, 3, 0], 'scores': [0.6412015557289124, 0.48419690132141113, 0.439375638961792, 0.6731411218643188, 0.6236090064048767, 0.5212202072143555, 0.6544840335845947, 0.5612025856971741, 0.5232595205307007, 0.4878042936325073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0079050064086914})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.044968843460083})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.106812834739685})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.103763222694397})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8082, 'crossentropy': 0.96121181640625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 5567], ['id', 14811], ['id', 45508], ['id', 38778], ['id', 13014], ['id', 1734], ['id', 4183], ['id', 39778], ['id', 1846], ['id', 48699]], 'labels': [3, 4, 3, 8, 8, 1, 2, 8, 7, 2], 'scores': [0.4505246877670288, 0.5775965452194214, 0.5107795000076294, 0.5701708793640137, 0.5962121486663818, 0.4525291919708252, 0.46776050329208374, 0.5035975575447083, 0.5238329172134399, 0.46740031242370605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9075923562049866})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8084352016448975})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8202093839645386})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9224331974983215})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9155738353729248})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8694, 'crossentropy': 0.659949951171875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 36072], ['id', 36409], ['id', 19280], ['id', 41151], ['id', 38698], ['id', 17551], ['id', 49317], ['id', 3450], ['id', 36281], ['id', 31746]], 'labels': [2, 3, 3, 7, 5, 9, 1, 4, 7, 5], 'scores': [0.6135865449905396, 0.4890661835670471, 0.6491476893424988, 0.5960069298744202, 0.5969727039337158, 0.5893049240112305, 0.28922778367996216, 0.4365220069885254, 0.7410452365875244, 0.49276673793792725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8501518964767456})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7848093509674072})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8823623657226562})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8286544680595398})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8766788244247437})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8813, 'crossentropy': 0.659420751953125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 3370], ['ood', 3895], ['id', 32421], ['id', 35498], ['id', 44326], ['id', 46524], ['id', 15395], ['id', 31293], ['ood', 27468], ['ood', 55629]], 'labels': [4, 8, 3, 3, 0, 6, 9, 8, 8, 5], 'scores': [0.7010113894939423, 0.42074906826019287, 0.7444828748703003, 0.7318440675735474, 0.4302830696105957, 0.7274231910705566, 0.4794425964355469, 0.6239084005355835, 0.3012279272079468, 0.48539161682128906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8181109428405762})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6417094469070435})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6414576172828674})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6871961355209351})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7142392992973328})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7361865043640137})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8999, 'crossentropy': 0.579089501953125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 3070], ['id', 12117], ['id', 43868], ['id', 40636], ['id', 55274], ['id', 17079], ['id', 23332], ['id', 10774], ['id', 23195], ['id', 53758]], 'labels': [1, 3, 3, 3, 6, 6, 5, 6, 6, 3], 'scores': [0.9326463341712952, 0.6835340857505798, 0.7224463820457458, 0.6636741757392883, 0.8873507380485535, 0.8838944435119629, 0.696667492389679, 0.7824515700340271, 0.7324187755584717, 0.6110202670097351]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8139989376068115})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6197693347930908})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6383541822433472})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6661929488182068})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6581119298934937})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9012, 'crossentropy': 0.5639568359375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 32573], ['id', 12137], ['id', 1213], ['id', 16301], ['id', 58101], ['id', 5221], ['id', 9608], ['id', 782], ['id', 42059], ['id', 22612]], 'labels': [8, 5, 2, 8, 4, 1, 8, 9, 9, 2], 'scores': [0.46055924892425537, 0.5227193832397461, 0.7211136817932129, 0.558721661567688, 0.40525662899017334, 0.5090504884719849, 0.7903872728347778, 0.5520080327987671, 0.7828893065452576, 0.5136821866035461]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.845819354057312})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5855690836906433})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5722901821136475})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.566402018070221})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.582438051700592})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5927988886833191})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.669690728187561})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9228, 'crossentropy': 0.50199326171875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 29472], ['id', 15987], ['id', 2888], ['id', 4784], ['id', 19590], ['id', 54170], ['id', 28838], ['id', 38409], ['id', 41924], ['ood', 42085]], 'labels': [9, 9, 4, 7, 5, 9, 9, 2, 9, 5], 'scores': [0.750457227230072, 0.7645941972732544, 0.6985898613929749, 0.7646896541118622, 0.8616940379142761, 0.6774476170539856, 0.8876903057098389, 0.6320395767688751, 0.8783223032951355, 0.3945840001106262]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8418251276016235})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5922937989234924})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.524259626865387})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5152429938316345})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5688279867172241})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5063613653182983})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5560688972473145})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.557282030582428})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.54010009765625})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9318, 'crossentropy': 0.46414375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 55268], ['id', 13827], ['id', 46379], ['id', 13961], ['id', 33576], ['id', 10438], ['id', 57773], ['id', 42671], ['id', 33593], ['id', 38920]], 'labels': [8, 3, 3, 1, 9, 9, 8, 2, 2, 7], 'scores': [0.7250015139579773, 0.6986877918243408, 0.8224050998687744, 0.5807574391365051, 0.9027012288570404, 0.8666642308235168, 0.645146369934082, 0.7438066005706787, 0.748578667640686, 0.7259624004364014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7475394010543823})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49339163303375244})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4864230453968048})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4515252709388733})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48814743757247925})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4681634306907654})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5045080184936523})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.94, 'crossentropy': 0.3965247314453125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 37688], ['id', 53029], ['id', 28757], ['id', 27673], ['id', 2845], ['id', 49509], ['id', 16282], ['id', 8116], ['id', 50905], ['id', 17406]], 'labels': [9, 2, 3, 2, 8, 8, 8, 0, 7, 4], 'scores': [0.6396260857582092, 0.8023687601089478, 0.7446867227554321, 0.6271194219589233, 0.7364603281021118, 0.5965787768363953, 0.7556849718093872, 0.7915024757385254, 0.6080853343009949, 0.7319961786270142]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8466651439666748})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5287125110626221})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5150012373924255})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4626387357711792})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49118274450302124})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5310992002487183})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4745115041732788})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9414, 'crossentropy': 0.4027396484375}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 42454], ['id', 52688], ['ood', 9425], ['id', 53844], ['id', 41357], ['id', 23317], ['id', 3032], ['id', 43198], ['id', 47443], ['id', 3691]], 'labels': [2, 6, 6, 5, 0, 6, 8, 3, 2, 0], 'scores': [0.4694589376449585, 0.6366299390792847, 0.3924964666366577, 0.6250934600830078, 0.45373350381851196, 0.805355966091156, 0.6456032991409302, 0.7206228375434875, 0.6651485562324524, 0.8323298096656799]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.955963134765625})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5566420555114746})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4654417634010315})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4534909129142761})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.442664235830307})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45239126682281494})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5010582208633423})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47150707244873047})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9445, 'crossentropy': 0.4003300537109375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 53130], ['ood', 41557], ['id', 43702], ['id', 33697], ['id', 13109], ['id', 46576], ['id', 59584], ['id', 28657], ['id', 43796], ['id', 12453]], 'labels': [4, 7, 3, 2, 3, 5, 5, 5, 7, 7], 'scores': [0.4860798120498657, 0.5423585176467896, 0.7836639881134033, 0.6628468036651611, 0.7517076730728149, 0.6483023166656494, 0.6007912158966064, 0.5121369361877441, 0.8857482075691223, 0.6619800925254822]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8121830821037292})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5072077512741089})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48203903436660767})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.42226842045783997})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.41096797585487366})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4943426251411438})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4822404980659485})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.46388596296310425})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9466, 'crossentropy': 0.364259130859375}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 8693], ['id', 58535], ['id', 528], ['ood', 28110], ['id', 42931], ['id', 14697], ['id', 59309], ['id', 56014], ['id', 17574], ['id', 54932]], 'labels': [3, 5, 8, 5, 3, 8, 8, 5, 3, 5], 'scores': [0.6903823614120483, 0.8188150525093079, 0.8004441261291504, 0.4002406597137451, 0.7817729115486145, 0.732324481010437, 0.62518310546875, 0.6858842372894287, 0.6622601747512817, 0.7340831756591797]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0516815185546875})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.59639972448349})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4962420165538788})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4501776397228241})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4239024519920349})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4432904124259949})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45901697874069214})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43636131286621094})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9434, 'crossentropy': 0.3789682861328125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 59401], ['ood', 15738], ['id', 57659], ['id', 48953], ['id', 28512], ['id', 8838], ['id', 50426], ['id', 17772], ['id', 8214], ['id', 11797]], 'labels': [4, 2, 0, 4, 5, 0, 7, 7, 7, 3], 'scores': [0.6570789813995361, 0.6382317543029785, 0.5701411366462708, 0.5313324332237244, 0.8898720741271973, 0.7334288656711578, 0.7736595869064331, 0.5596010088920593, 0.7355342507362366, 0.5580087900161743]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0700905323028564})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5959678292274475})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4878780245780945})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48120778799057007})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48393285274505615})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4311857223510742})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43641600012779236})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46784496307373047})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4394787847995758})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9458, 'crossentropy': 0.37750107421875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 40646], ['id', 37347], ['id', 5170], ['id', 42472], ['id', 28592], ['id', 56451], ['id', 19148], ['id', 53204], ['id', 25421], ['id', 36818]], 'labels': [8, 2, 8, 2, 9, 7, 8, 9, 1, 7], 'scores': [0.9402718544006348, 0.8963778018951416, 0.6532263159751892, 1.0801551938056946, 0.7920893430709839, 0.6762666702270508, 0.6363356113433838, 0.6360947489738464, 0.5440250039100647, 0.7994042038917542]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0441782474517822})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5468336343765259})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.41566887497901917})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.42288973927497864})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42007187008857727})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4014531970024109})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4202856123447418})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4362437129020691})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44893357157707214})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.951, 'crossentropy': 0.3751267822265625}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 22670], ['id', 58855], ['id', 46157], ['id', 58560], ['id', 52729], ['id', 57276], ['id', 16860], ['id', 54880], ['id', 31667], ['id', 47611]], 'labels': [4, 3, 3, 0, 4, 8, 8, 5, 3, 6], 'scores': [0.7160434126853943, 0.8221832513809204, 0.8356829285621643, 0.8639458417892456, 0.8361760377883911, 0.7073512077331543, 0.8159387409687042, 0.8480663299560547, 0.7806002497673035, 0.7648175954818726]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.021943211555481})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5601537227630615})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.43632185459136963})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.40207821130752563})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.42145055532455444})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37135010957717896})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4158485531806946})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4106343984603882})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4128449559211731})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9562, 'crossentropy': 0.3438094482421875}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 30451], ['id', 36415], ['id', 13373], ['id', 52890], ['id', 21896], ['id', 29249], ['ood', 25135], ['id', 30525], ['id', 36450], ['id', 36714]], 'labels': [8, 6, 6, 8, 8, 3, 5, 8, 2, 6], 'scores': [0.7200449705123901, 0.6918092966079712, 0.6454452276229858, 0.7669589519500732, 1.032103419303894, 0.6933053135871887, 0.35898780822753906, 0.5183616280555725, 0.8218376040458679, 0.8182671666145325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.901636004447937})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5094550251960754})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3764899969100952})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37664175033569336})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3357159495353699})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3615977168083191})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32409435510635376})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37935665249824524})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34412848949432373})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3428787887096405})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9556, 'crossentropy': 0.3146377685546875}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 50429], ['id', 36126], ['id', 27299], ['id', 57882], ['id', 24944], ['ood', 28218], ['id', 45094], ['id', 59731], ['id', 13752], ['id', 40824]], 'labels': [8, 5, 8, 0, 6, 2, 2, 5, 9, 5], 'scores': [0.6255353093147278, 0.8629088401794434, 0.6134770810604095, 0.8444432020187378, 0.4738328456878662, 0.5472695827484131, 0.9292130470275879, 0.7160519957542419, 0.928806483745575, 0.8282774090766907]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0522499084472656})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5576947927474976})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42570745944976807})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39308810234069824})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3678285777568817})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41319698095321655})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3964959681034088})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3533085584640503})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3619847297668457})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3677179217338562})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3838205337524414})
store['active_learning_steps'][23]['training']['best_epoch']=8
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9635, 'crossentropy': 0.2904599853515625}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 11858], ['id', 52173], ['id', 5103], ['id', 47870], ['id', 8780], ['id', 8093], ['id', 18480], ['id', 14619], ['id', 47387], ['id', 27852]], 'labels': [8, 7, 2, 9, 8, 0, 2, 3, 8, 2], 'scores': [0.8555578589439392, 0.8959241211414337, 0.9437785744667053, 0.8726711273193359, 0.6981799006462097, 0.906170666217804, 0.5719764530658722, 0.8534116148948669, 0.6936713457107544, 0.6853541433811188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.2979273796081543})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6368311643600464})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4480360150337219})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3930089473724365})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38931378722190857})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34772443771362305})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3477837145328522})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3223643898963928})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.36694151163101196})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.357217013835907})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3628368377685547})
store['active_learning_steps'][24]['training']['best_epoch']=8
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9602, 'crossentropy': 0.330083447265625}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 42648], ['id', 34829], ['ood', 25216], ['id', 41196], ['id', 19208], ['id', 32002], ['ood', 26844], ['id', 38316], ['id', 11240], ['ood', 20349]], 'labels': [5, 5, 0, 9, 6, 6, 1, 4, 0, 5], 'scores': [0.5026566982269287, 0.9170082211494446, 0.506494402885437, 0.8631641268730164, 0.5191359519958496, 0.8724091053009033, 0.3371155261993408, 0.739317774772644, 0.9322212934494019, 0.273545503616333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0326343774795532})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5773895978927612})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.399425745010376})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3480873107910156})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30742156505584717})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32875174283981323})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3431701064109802})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3507685959339142})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.2871070556640625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 33830], ['id', 15835], ['id', 35633], ['id', 48512], ['id', 56086], ['id', 30932], ['id', 8954], ['id', 53242], ['id', 53872], ['id', 19981]], 'labels': [7, 1, 7, 5, 7, 0, 7, 7, 8, 8], 'scores': [0.5598918199539185, 0.4312402009963989, 0.6641841530799866, 0.6965986490249634, 0.5950201749801636, 0.6818356513977051, 0.6096193790435791, 0.6078599691390991, 0.7914676666259766, 0.5314051806926727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1867074966430664})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5713603496551514})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40291398763656616})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36570143699645996})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33920300006866455})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3148595094680786})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34795114398002625})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3043505549430847})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.349608838558197})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.368019700050354})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35040295124053955})
store['active_learning_steps'][26]['training']['best_epoch']=8
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.2855119873046875}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 45911], ['id', 16044], ['id', 32747], ['id', 2236], ['id', 40876], ['id', 48382], ['id', 49889], ['id', 51025], ['id', 15781], ['id', 30844]], 'labels': [3, 8, 8, 4, 9, 8, 0, 7, 5, 8], 'scores': [0.8176821172237396, 0.6851301789283752, 0.9143099188804626, 0.8816038370132446, 0.5828790962696075, 1.0062201023101807, 0.5650882124900818, 0.691118061542511, 0.7294617891311646, 0.9689823985099792]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.233433485031128})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5502196550369263})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39171916246414185})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38157570362091064})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34208744764328003})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35901960730552673})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.324424684047699})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3149152398109436})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35616469383239746})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3360896110534668})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34092554450035095})
store['active_learning_steps'][27]['training']['best_epoch']=8
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.27889189453125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 5771], ['id', 43208], ['id', 9390], ['id', 30144], ['id', 12206], ['id', 49634], ['id', 25096], ['id', 23086], ['id', 56457], ['id', 37778]], 'labels': [5, 3, 9, 9, 7, 8, 5, 8, 3, 8], 'scores': [0.6909105181694031, 0.570434033870697, 0.8157448768615723, 0.7627587914466858, 0.49902260303497314, 0.6098850965499878, 0.7917130589485168, 0.7215026617050171, 0.9102125763893127, 0.8796457052230835]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.230411410331726})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.6024577617645264})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.43403488397598267})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38952624797821045})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3507053256034851})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3412025272846222})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3434253931045532})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3078728914260864})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3007909655570984})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3126726746559143})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2904163599014282})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3256000280380249})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3264662027359009})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31355613470077515})
store['active_learning_steps'][28]['training']['best_epoch']=11
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9729, 'crossentropy': 0.2547949462890625}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 50789], ['ood', 24128], ['id', 52086], ['id', 8772], ['id', 11099], ['id', 20623], ['id', 10195], ['ood', 9821], ['id', 54492], ['id', 43001]], 'labels': [1, 8, 5, 1, 7, 9, 0, 8, 8, 9], 'scores': [0.7710100412368774, 0.506027340888977, 0.8139393329620361, 0.6632757186889648, 0.5108468234539032, 0.9523366689682007, 0.7075096368789673, 0.6284137964248657, 0.6370545923709869, 0.5714472532272339]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.3458869457244873})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5884937047958374})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4656239151954651})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38950759172439575})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36759695410728455})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2966806888580322})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3202260732650757})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.31743547320365906})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3741879165172577})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.272499853515625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 42415], ['id', 40654], ['id', 14749], ['id', 34532], ['id', 30493], ['id', 40585], ['id', 854], ['id', 13243], ['id', 966], ['id', 40236]], 'labels': [7, 5, 0, 2, 1, 9, 2, 7, 3, 4], 'scores': [0.7645544409751892, 0.6887273192405701, 0.7648351788520813, 0.4752202033996582, 0.7576872110366821, 0.5042687952518463, 0.6091011166572571, 0.607500433921814, 0.6742441058158875, 0.6049774885177612]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.4893229007720947})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.7507174015045166})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.47802799940109253})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3891056776046753})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34639424085617065})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31556805968284607})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33305931091308594})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3562735319137573})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32788094878196716})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.296066357421875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 995], ['id', 23042], ['id', 14935], ['id', 52294], ['id', 17544], ['id', 8082], ['id', 49914], ['id', 12874], ['id', 30658], ['id', 38287]], 'labels': [7, 9, 3, 0, 5, 2, 2, 3, 4, 5], 'scores': [0.5059248208999634, 0.4077622890472412, 0.9360663890838623, 0.8204033970832825, 0.3931310772895813, 0.2820074260234833, 0.47945165634155273, 0.5608737468719482, 0.6786348223686218, 0.5015637278556824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2663321495056152})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5900024175643921})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.44753849506378174})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37066614627838135})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33416733145713806})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29095691442489624})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2865979075431824})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3270023465156555})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2964310944080353})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29031142592430115})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9701, 'crossentropy': 0.2663873046875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 7058], ['id', 17507], ['id', 44256], ['id', 57290], ['id', 14650], ['id', 54030], ['id', 43745], ['id', 57024], ['id', 44969], ['id', 58249]], 'labels': [3, 2, 4, 9, 4, 8, 8, 9, 3, 3], 'scores': [0.5729817748069763, 0.7088954448699951, 0.38565149903297424, 0.5114176273345947, 0.6568881273269653, 0.8651965260505676, 0.7566515207290649, 0.6424707770347595, 0.6552829742431641, 0.5488267540931702]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.3002281188964844})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8099299669265747})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4342767894268036})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4142651855945587})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3454495668411255})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3343279957771301})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3269883990287781})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34782055020332336})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35054081678390503})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31316667795181274})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3303229510784149})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36430710554122925})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3011033535003662})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33086878061294556})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35908782482147217})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.38567593693733215})
store['active_learning_steps'][32]['training']['best_epoch']=13
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.282162255859375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 8045], ['id', 52686], ['id', 19103], ['id', 21495], ['id', 11738], ['id', 52550], ['id', 50454], ['id', 28932], ['id', 41772], ['id', 47201]], 'labels': [8, 5, 8, 9, 2, 2, 2, 2, 5, 8], 'scores': [0.8331414461135864, 0.658844530582428, 0.36272355914115906, 0.8217073678970337, 0.6329537332057953, 0.86440709233284, 0.8930674195289612, 0.9119810461997986, 0.9234065413475037, 0.5601407885551453]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.1636523008346558})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.6085439920425415})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4567767381668091})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.33007240295410156})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3528136610984802})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31658196449279785})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3396036922931671})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3086943030357361})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31353792548179626})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3056832551956177})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3628823459148407})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31833410263061523})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28990545868873596})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3450719118118286})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3245851993560791})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.33257874846458435})
store['active_learning_steps'][33]['training']['best_epoch']=13
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.250706201171875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 52225], ['id', 12986], ['id', 54981], ['id', 28368], ['id', 57665], ['id', 49437], ['id', 32702], ['id', 37122], ['id', 50180], ['id', 50618]], 'labels': [2, 5, 2, 9, 8, 1, 5, 8, 8, 6], 'scores': [0.7124630212783813, 0.8938969373703003, 0.6415324211120605, 0.8738327622413635, 0.8734005093574524, 0.40778088569641113, 0.6894873082637787, 0.8268751502037048, 0.5659514367580414, 0.5839047431945801]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.227357268333435})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.5734597444534302})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4403887987136841})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37740492820739746})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32245153188705444})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3237971067428589})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30708104372024536})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3349795937538147})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30414485931396484})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2917029559612274})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.332172691822052})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30998361110687256})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3217071294784546})
store['active_learning_steps'][34]['training']['best_epoch']=10
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.2672406982421875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 57714], ['id', 39673], ['id', 43852], ['id', 54885], ['id', 21598], ['id', 23962], ['id', 19702], ['id', 51230], ['id', 4873], ['id', 22139]], 'labels': [1, 2, 2, 6, 2, 3, 5, 3, 8, 2], 'scores': [0.8191685676574707, 0.7346940040588379, 0.7837542295455933, 0.783772885799408, 0.7561037540435791, 0.7749926447868347, 0.8397252559661865, 0.7182155847549438, 0.8268349170684814, 0.908607542514801]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1040680408477783})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.6146460175514221})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.43723559379577637})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3625560998916626})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3194645047187805})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28661832213401794})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2756505012512207})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26971709728240967})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27710819244384766})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26238417625427246})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2732686698436737})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2825596034526825})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28998520970344543})
store['active_learning_steps'][35]['training']['best_epoch']=10
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9762, 'crossentropy': 0.2446425048828125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 13412], ['id', 56838], ['id', 37221], ['id', 20641], ['id', 14305], ['id', 27706], ['id', 49910], ['id', 39208], ['id', 52135], ['id', 16572]], 'labels': [8, 5, 4, 9, 8, 7, 6, 5, 0, 4], 'scores': [0.9227557182312012, 0.6029477119445801, 0.8249731957912445, 0.944275438785553, 0.746856689453125, 0.7283432483673096, 1.0702317953109741, 0.8088524341583252, 0.5731881856918335, 0.6985070705413818]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1340343952178955})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6262046098709106})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4647727608680725})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3466925621032715})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31795036792755127})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2812078893184662})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3128701448440552})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2674790024757385})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2803913652896881})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3213235139846802})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2793184220790863})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9727, 'crossentropy': 0.2552273681640625}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 14845], ['id', 29863], ['id', 26574], ['id', 30986], ['id', 11702], ['id', 50632], ['id', 46135], ['id', 46345], ['id', 41100], ['id', 57742]], 'labels': [8, 8, 5, 3, 1, 1, 8, 2, 0, 6], 'scores': [0.4994794726371765, 0.6678346991539001, 0.673104465007782, 0.8101640939712524, 0.4563537836074829, 0.7770559787750244, 0.6333624124526978, 0.49108269810676575, 0.3243024945259094, 0.7792827486991882]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.1492218971252441})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6353821158409119})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4699903130531311})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40704795718193054})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3366240859031677})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3155354857444763})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32904404401779175})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31992748379707336})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32164061069488525})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9671, 'crossentropy': 0.285397900390625}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 12297], ['id', 31284], ['id', 1674], ['id', 31988], ['id', 46300], ['id', 30900], ['id', 30792], ['id', 59653], ['id', 50431], ['id', 21601]], 'labels': [9, 7, 9, 3, 5, 5, 4, 0, 3, 1], 'scores': [0.6278350353240967, 0.6187269687652588, 1.0414801836013794, 0.6631624102592468, 0.7036424279212952, 0.6962065696716309, 0.7659811973571777, 0.7313621640205383, 0.778927743434906, 0.7861227989196777]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.255995512008667})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6310949325561523})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4365667998790741})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.38315123319625854})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32868969440460205})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3054811656475067})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29397571086883545})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28876733779907227})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2576320767402649})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.290580689907074})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2674873471260071})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27744150161743164})
store['active_learning_steps'][38]['training']['best_epoch']=9
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9752, 'crossentropy': 0.2379050537109375}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 29879], ['id', 19124], ['id', 24136], ['id', 36970], ['id', 45069], ['id', 27737], ['id', 57124], ['id', 46375], ['id', 7851], ['id', 16622]], 'labels': [4, 8, 1, 4, 4, 1, 5, 0, 8, 9], 'scores': [0.8112469911575317, 0.6444804668426514, 0.5105633735656738, 0.5711670219898224, 0.8102759718894958, 0.43413543701171875, 0.43633797764778137, 0.5685601532459259, 0.8671485781669617, 0.7053830027580261]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.2654838562011719})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6249523162841797})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.44323909282684326})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33199769258499146})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2947750985622406})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.3002372980117798})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2769692540168762})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2629603147506714})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27014002203941345})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26885879039764404})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2967583239078522})
store['active_learning_steps'][39]['training']['best_epoch']=8
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9752, 'crossentropy': 0.233440380859375}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 55738], ['id', 19501], ['id', 43822], ['id', 51600], ['id', 49579], ['id', 51764], ['id', 12646], ['id', 6418], ['id', 57956], ['id', 30024]], 'labels': [6, 3, 6, 4, 8, 5, 9, 5, 2, 6], 'scores': [0.7099108695983887, 0.6426109075546265, 0.6633556485176086, 0.8873690366744995, 0.442624032497406, 0.7739816308021545, 0.4883071482181549, 0.8106677532196045, 0.7226736545562744, 0.5906751453876495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.3092095851898193})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5883913040161133})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.42065632343292236})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3431292176246643})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3181883692741394})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2735356390476227})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27271604537963867})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25093162059783936})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2842605710029602})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25770020484924316})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3038939833641052})
store['active_learning_steps'][40]['training']['best_epoch']=8
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9746, 'crossentropy': 0.24394541015625}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 39424], ['ood', 44410], ['id', 52761], ['id', 47844], ['id', 45944], ['id', 35630], ['id', 39779], ['id', 47076], ['id', 12651], ['id', 42673]], 'labels': [5, 1, 9, 7, 9, 2, 8, 8, 9, 1], 'scores': [0.3963141143321991, 0.27371644973754883, 0.5881096720695496, 0.7478117346763611, 0.6795783042907715, 0.547931969165802, 0.5280649065971375, 0.505400151014328, 0.7409399747848511, 0.7490724325180054]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2653627395629883})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6307429075241089})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41381722688674927})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32517755031585693})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31229284405708313})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31387871503829956})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2890065908432007})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2557157576084137})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2610270380973816})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2580086290836334})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26227840781211853})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9739, 'crossentropy': 0.2390357177734375}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 12868], ['id', 23486], ['id', 54399], ['id', 33158], ['id', 6746], ['id', 47506], ['id', 41832], ['id', 28392], ['id', 50403], ['id', 26850]], 'labels': [9, 4, 4, 2, 8, 8, 2, 3, 3, 2], 'scores': [0.6407591104507446, 0.7588644027709961, 0.2849341928958893, 0.6342810988426208, 0.6145213842391968, 0.709594190120697, 0.67503821849823, 0.7957555055618286, 0.6573352813720703, 0.8077240586280823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3154587745666504})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6741585731506348})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.48572713136672974})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3501278758049011})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3100699186325073})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.308025598526001})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27932554483413696})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2570025622844696})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2803666591644287})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2714719772338867})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28474462032318115})
store['active_learning_steps'][42]['training']['best_epoch']=8
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.975, 'crossentropy': 0.234366259765625}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 15774], ['id', 15829], ['id', 8463], ['id', 32393], ['id', 59286], ['id', 40066], ['id', 29476], ['id', 12742], ['id', 1380], ['id', 32475]], 'labels': [3, 2, 7, 5, 8, 4, 3, 7, 4, 2], 'scores': [0.6485434770584106, 0.6847431659698486, 0.6027499437332153, 0.6902616024017334, 0.7611134648323059, 0.8849354982376099, 0.7693967819213867, 0.5611054301261902, 0.6820244789123535, 0.6516015529632568]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.2594331502914429})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.6578324437141418})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4488323926925659})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34328287839889526})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29533320665359497})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2753077447414398})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3114323914051056})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26907917857170105})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29882171750068665})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2901836633682251})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28193989396095276})
store['active_learning_steps'][43]['training']['best_epoch']=8
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9751, 'crossentropy': 0.2284259765625}
