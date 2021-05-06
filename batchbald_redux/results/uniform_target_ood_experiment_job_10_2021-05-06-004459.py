store = {}
store['timestamp']=1620258299
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=10']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=10
store['worker_id']=10
store['num_workers']=40
store['config']={'seed': 12, 'acquisition_size': 20, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.1685566902160645})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.5789003372192383})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.7932701110839844})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.9554247856140137})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6665, 'crossentropy': 1.9989484375}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 15503], ['id', 18105], ['id', 44331], ['id', 8450], ['id', 57882], ['id', 35187], ['id', 10738], ['id', 3496], ['id', 20547], ['id', 10986], ['id', 12985], ['id', 34524], ['id', 32655], ['id', 41700], ['id', 57326], ['id', 47635], ['id', 1000], ['id', 53282], ['id', 21155], ['id', 8190]], 'labels': [9, 6, 6, 3, 0, 5, 8, 4, 5, 7, 2, 8, 7, 7, 0, 8, 0, 3, 5, 5], 'scores': [1.0020350813865662, 0.7118675708770752, 0.7261292338371277, 0.7072409987449646, 1.0074518918991089, 0.8230825662612915, 0.7577382922172546, 0.8964368104934692, 0.9383977651596069, 0.9570090770721436, 0.616812527179718, 0.920036256313324, 0.7455303072929382, 0.7331569194793701, 0.9639536738395691, 0.9169168472290039, 0.8128551840782166, 0.5751502513885498, 0.9478236436843872, 0.8162726759910583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.4390355348587036})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.5595877170562744})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.6446435451507568})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.7803857326507568})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7547, 'crossentropy': 1.26663896484375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 55727], ['id', 32874], ['id', 19770], ['id', 28669], ['id', 38301], ['id', 20254], ['id', 51476], ['id', 36853], ['id', 20268], ['id', 46800], ['id', 17179], ['id', 42482], ['id', 24531], ['id', 1099], ['id', 19350], ['id', 1148], ['ood', 13132], ['id', 1129], ['ood', 44335], ['id', 40562]], 'labels': [0, 8, 0, 4, 4, 9, 6, 2, 2, 9, 8, 9, 3, 4, 8, 1, 6, 2, 8, 2], 'scores': [0.902881383895874, 0.447390079498291, 0.6551505327224731, 0.6948460340499878, 0.6086134314537048, 0.5557719469070435, 0.5785022377967834, 0.7211984395980835, 0.8048185110092163, 0.7163726091384888, 0.31627655029296875, 0.670985758304596, 0.6778548955917358, 0.5989563465118408, 0.7659388780593872, 0.563135027885437, 0.3578073978424072, 0.5969979166984558, 0.4188622236251831, 0.7320483326911926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.0994822978973389})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.106657862663269})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.3316612243652344})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.385831356048584})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7966, 'crossentropy': 0.97051396484375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 24653], ['id', 47417], ['id', 41557], ['id', 14277], ['id', 29904], ['id', 7757], ['id', 38343], ['id', 5920], ['id', 55146], ['id', 17153], ['id', 44620], ['id', 45917], ['id', 49354], ['id', 5258], ['id', 13885], ['id', 13715], ['id', 4147], ['id', 14619], ['id', 44382], ['id', 29289]], 'labels': [4, 7, 0, 7, 2, 9, 4, 6, 8, 2, 4, 9, 0, 2, 8, 6, 8, 3, 6, 3], 'scores': [0.618437647819519, 0.47665631771087646, 0.6296253800392151, 0.44125139713287354, 0.7563578486442566, 0.420352041721344, 0.6973796486854553, 0.6438778042793274, 0.5595716238021851, 0.6388262510299683, 0.5000924468040466, 0.5344028472900391, 0.7329977750778198, 0.4874541163444519, 0.5835294127464294, 0.6150599718093872, 0.6164934635162354, 0.6668700575828552, 0.5924956202507019, 0.8591017127037048]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9149246215820312})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9347811937332153})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.015067219734192})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.091799259185791})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8425, 'crossentropy': 0.82065283203125}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 192], ['id', 6744], ['id', 39151], ['id', 41987], ['id', 7188], ['id', 42201], ['id', 45250], ['id', 50135], ['id', 43080], ['id', 39625], ['ood', 35205], ['id', 32343], ['id', 5979], ['id', 36157], ['id', 37106], ['id', 24673], ['id', 19959], ['id', 15695], ['id', 3694], ['id', 4058]], 'labels': [5, 8, 4, 0, 1, 3, 5, 6, 3, 5, 0, 5, 9, 7, 8, 6, 5, 0, 4, 8], 'scores': [0.43626558780670166, 0.46856367588043213, 0.511201024055481, 0.6025968194007874, 0.47649282217025757, 0.7338699102401733, 0.664992094039917, 0.5054134130477905, 0.517735481262207, 0.5078802108764648, 0.36918938159942627, 0.783235490322113, 0.5632442235946655, 0.648456871509552, 0.36711013317108154, 0.4598708152770996, 0.7206896543502808, 0.6148757934570312, 0.762701690196991, 0.7820477485656738]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7908908128738403})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7475574016571045})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7259677648544312})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7991129159927368})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8638341426849365})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8664536476135254})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8879, 'crossentropy': 0.64902939453125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 7493], ['id', 3288], ['id', 15064], ['id', 18262], ['id', 7581], ['id', 59934], ['id', 20120], ['id', 9738], ['id', 5580], ['id', 17489], ['id', 24740], ['id', 14951], ['id', 14878], ['id', 27984], ['id', 21371], ['id', 47655], ['id', 9948], ['id', 31290], ['id', 30600], ['id', 14001]], 'labels': [6, 6, 0, 6, 6, 0, 5, 5, 4, 2, 8, 5, 3, 7, 5, 3, 8, 5, 2, 1], 'scores': [0.7047807574272156, 0.7203335762023926, 0.5786466002464294, 0.40908345580101013, 0.7312598824501038, 0.6127982139587402, 0.7703077793121338, 0.6480951309204102, 0.574035108089447, 0.9128570556640625, 0.8794801235198975, 0.7015994787216187, 0.663150429725647, 0.7103031873703003, 0.7605668306350708, 0.6194570064544678, 0.8775028586387634, 0.7655501961708069, 0.7394334077835083, 0.5247985124588013]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7660608291625977})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5826650857925415})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5803012251853943})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5912862420082092})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6730408668518066})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6760072708129883})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.9256, 'crossentropy': 0.485126513671875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 27370], ['id', 7891], ['id', 55438], ['id', 27102], ['id', 38537], ['id', 846], ['id', 28200], ['id', 11979], ['id', 5983], ['id', 24111], ['id', 39047], ['id', 17621], ['id', 49495], ['id', 32310], ['id', 23768], ['id', 18776], ['id', 53120], ['id', 33001], ['id', 54350], ['id', 40599]], 'labels': [9, 8, 8, 4, 7, 6, 2, 3, 1, 3, 7, 3, 9, 4, 8, 2, 5, 5, 2, 5], 'scores': [0.5247234106063843, 0.6162800192832947, 0.6787848472595215, 0.4598488509654999, 0.6442628800868988, 0.8296641707420349, 0.5568068623542786, 0.7574320435523987, 0.39004623889923096, 0.5504243969917297, 0.7265052199363708, 0.5015867352485657, 0.5790019631385803, 0.5585339665412903, 0.5494901537895203, 0.5097360610961914, 0.9247016906738281, 0.7174668312072754, 0.6597550511360168, 0.7745656967163086]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7843540906906128})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6245313882827759})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5980935096740723})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5944922566413879})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6575267314910889})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6184955835342407})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6548416614532471})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.9233, 'crossentropy': 0.495139501953125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 28475], ['id', 27819], ['id', 966], ['id', 47548], ['id', 49529], ['id', 40743], ['id', 17375], ['id', 27406], ['id', 51173], ['id', 3870], ['id', 40305], ['id', 56199], ['id', 26574], ['id', 41349], ['ood', 24667], ['id', 25295], ['id', 41239], ['id', 12153], ['id', 25359], ['id', 26444]], 'labels': [8, 8, 3, 8, 3, 3, 8, 7, 3, 5, 3, 9, 5, 9, 7, 5, 9, 3, 5, 1], 'scores': [0.904163658618927, 0.7689821124076843, 0.5552659034729004, 0.8479797840118408, 0.9106049537658691, 0.7283987402915955, 0.8665532469749451, 0.7620823383331299, 0.6778128147125244, 0.7522665560245514, 0.7718482613563538, 0.8844311535358429, 0.961723268032074, 0.6774810552597046, 0.5719252824783325, 0.7166064977645874, 0.8616892099380493, 0.667561411857605, 0.8860044479370117, 0.9286327958106995]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8085903525352478})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5217239260673523})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5336273908615112})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49136894941329956})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.53040611743927})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5435956716537476})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5597978234291077})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.9368, 'crossentropy': 0.42675029296875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 24275], ['id', 41622], ['id', 24779], ['id', 47387], ['id', 15548], ['id', 45046], ['id', 14290], ['id', 11147], ['id', 18049], ['id', 24728], ['id', 49589], ['id', 49987], ['id', 48077], ['id', 35996], ['id', 34678], ['id', 30342], ['id', 7270], ['id', 34090], ['id', 14760], ['id', 470]], 'labels': [5, 8, 6, 8, 1, 3, 4, 2, 3, 2, 3, 0, 9, 9, 8, 9, 5, 9, 2, 1], 'scores': [0.5225045680999756, 0.7411497831344604, 0.4680590331554413, 0.684200644493103, 0.5139329433441162, 0.6304444670677185, 0.6143010258674622, 0.7507243156433105, 0.8323314785957336, 0.5533060431480408, 0.6408974528312683, 0.6759594678878784, 0.6110119223594666, 0.7188249826431274, 0.6243352890014648, 0.540739119052887, 0.6861965656280518, 0.6968979835510254, 0.6336931586265564, 0.6511905193328857]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8777928948402405})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5011436343193054})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5099072456359863})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49633359909057617})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5369138121604919})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5263345837593079})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5793187618255615})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.9412, 'crossentropy': 0.442280859375}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 43897], ['ood', 47626], ['id', 47260], ['id', 26998], ['id', 56271], ['id', 14632], ['id', 54032], ['id', 31390], ['id', 7207], ['id', 25873], ['id', 28664], ['id', 59718], ['id', 16729], ['id', 35954], ['id', 15592], ['id', 27740], ['id', 42115], ['id', 54035], ['id', 39309], ['id', 52173]], 'labels': [1, 5, 6, 3, 9, 6, 6, 8, 2, 8, 8, 8, 2, 3, 9, 8, 2, 7, 0, 7], 'scores': [0.7405823469161987, 0.6965405941009521, 0.8236373066902161, 0.6807954907417297, 0.6218318939208984, 0.5737071633338928, 0.8046853542327881, 0.7794266939163208, 0.7089654207229614, 1.0233792066574097, 0.553756445646286, 0.6914121508598328, 0.6529816687107086, 0.6365644335746765, 0.8661317825317383, 0.6575531363487244, 0.8446184396743774, 0.6752821207046509, 0.4600679278373718, 0.8042405843734741]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7921411991119385})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4851619005203247})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4975185990333557})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44804391264915466})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.431546688079834})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.46105676889419556})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.45180749893188477})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4788312315940857})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9463, 'crossentropy': 0.372702685546875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 10503], ['id', 20363], ['id', 12950], ['id', 58430], ['id', 578], ['id', 6251], ['id', 16678], ['id', 14665], ['ood', 54888], ['id', 56838], ['id', 26034], ['id', 37974], ['id', 58470], ['id', 40093], ['id', 7000], ['id', 12655], ['id', 27336], ['id', 12514], ['id', 17079], ['id', 27678]], 'labels': [6, 8, 2, 6, 6, 3, 3, 8, 7, 5, 5, 2, 9, 6, 8, 9, 1, 2, 6, 8], 'scores': [0.4691261053085327, 0.9059590697288513, 0.7682536840438843, 0.5646843910217285, 0.6693457961082458, 0.6180428266525269, 0.7582994699478149, 0.7025057673454285, 0.41629934310913086, 0.5671460628509521, 0.6478779911994934, 0.7932769060134888, 0.9130051732063293, 0.4248199462890625, 0.7844430208206177, 0.9189677238464355, 0.47864776849746704, 0.8404293060302734, 0.9715260863304138, 0.8447296619415283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8967642784118652})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5210771560668945})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46547651290893555})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41012874245643616})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.421430766582489})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39527758955955505})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41431838274002075})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47210603952407837})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4153766930103302})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.956, 'crossentropy': 0.3229101806640625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 33408], ['id', 32776], ['id', 20170], ['id', 22725], ['id', 29827], ['id', 55190], ['ood', 12248], ['id', 31200], ['id', 27716], ['ood', 7058], ['id', 52462], ['id', 11858], ['id', 13526], ['id', 17634], ['id', 29564], ['id', 47291], ['id', 10716], ['id', 45454], ['id', 56220], ['id', 48726]], 'labels': [7, 4, 9, 9, 4, 3, 1, 9, 7, 1, 9, 8, 9, 3, 0, 1, 7, 8, 7, 8], 'scores': [0.8258526921272278, 0.8639849424362183, 0.7507514357566833, 0.6865355372428894, 0.8586215376853943, 0.7730740904808044, 0.4712332487106323, 0.7407531142234802, 0.562099814414978, 0.5960203409194946, 0.8959641456604004, 0.5623908340930939, 0.9808654189109802, 0.7352325320243835, 0.7234860062599182, 0.8791378736495972, 0.8318654894828796, 0.5866825580596924, 0.6936651468276978, 0.7790159583091736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9826599359512329})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5229699611663818})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3864395022392273})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36980682611465454})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3958590030670166})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4012499451637268})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3924073576927185})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9526, 'crossentropy': 0.3438508056640625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 7833], ['id', 48767], ['id', 4480], ['id', 5740], ['id', 37360], ['id', 12484], ['id', 28312], ['id', 10048], ['ood', 15135], ['id', 53044], ['id', 37584], ['id', 39373], ['id', 1239], ['id', 24542], ['id', 38122], ['id', 21449], ['id', 31668], ['id', 56401], ['id', 39464], ['id', 56702]], 'labels': [5, 2, 5, 9, 2, 5, 4, 1, 7, 9, 5, 8, 8, 4, 4, 9, 4, 9, 9, 9], 'scores': [0.81972736120224, 0.6482517719268799, 0.43694639205932617, 0.7568179965019226, 0.7043856978416443, 0.7820658087730408, 0.5387455224990845, 0.511570930480957, 0.39404845237731934, 0.5073304772377014, 0.7235691547393799, 0.6632313132286072, 0.7847647070884705, 0.6471022963523865, 0.6401359438896179, 0.59731525182724, 0.42887693643569946, 0.7371553182601929, 0.513178825378418, 0.7111034393310547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.044600248336792})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5380465388298035})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4210505783557892})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40078145265579224})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3967586159706116})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34076905250549316})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37287524342536926})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38280627131462097})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3768552839756012})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9569, 'crossentropy': 0.313947900390625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 16027], ['id', 15521], ['id', 27172], ['id', 50562], ['id', 43206], ['id', 7083], ['id', 7886], ['id', 56183], ['id', 20811], ['id', 17019], ['id', 5798], ['id', 278], ['id', 37610], ['id', 41283], ['id', 38810], ['id', 45056], ['id', 49052], ['id', 50090], ['id', 12151], ['id', 138]], 'labels': [2, 4, 3, 9, 5, 4, 9, 4, 9, 9, 3, 5, 2, 3, 7, 8, 8, 4, 3, 5], 'scores': [0.7057639360427856, 0.5045718252658844, 0.9783998131752014, 0.8913525640964508, 0.770237922668457, 0.6784602999687195, 0.7248003482818604, 0.6840747594833374, 0.943488597869873, 1.0095611810684204, 0.6732621192932129, 0.7079000473022461, 0.866645336151123, 0.7604930996894836, 0.5361151993274689, 0.8150791525840759, 0.5850808024406433, 0.9136607050895691, 0.7020672559738159, 0.5533411800861359]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.841109037399292})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.46454793214797974})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3450952172279358})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3332240581512451})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36873435974121094})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.329246461391449})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.317852258682251})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3483245372772217})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34876686334609985})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3709377646446228})
store['active_learning_steps'][13]['training']['best_epoch']=7
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.27443203125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 2064], ['id', 6466], ['id', 25159], ['id', 49517], ['id', 48991], ['id', 37118], ['id', 19902], ['id', 24608], ['id', 30452], ['id', 44570], ['id', 53559], ['id', 2582], ['id', 15679], ['id', 2580], ['id', 43626], ['id', 8765], ['id', 14305], ['id', 45944], ['id', 19507], ['id', 31876]], 'labels': [7, 2, 0, 6, 2, 3, 0, 5, 9, 7, 4, 0, 2, 3, 4, 3, 8, 9, 1, 9], 'scores': [0.7147231101989746, 0.8843978047370911, 0.7191678285598755, 0.8548893332481384, 0.6550599336624146, 0.6410272717475891, 0.49164557456970215, 0.7149264812469482, 0.6507883667945862, 0.7001240253448486, 0.7606774568557739, 0.43896007537841797, 0.9711326360702515, 0.8264041543006897, 0.7166502475738525, 0.6076579093933105, 0.7928172945976257, 0.6661602258682251, 0.8002433180809021, 0.6263682246208191]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.9524073004722595})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.49244314432144165})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36189109086990356})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31418782472610474})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3320840895175934})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3229372501373291})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3164902925491333})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9675, 'crossentropy': 0.274316943359375}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 27971], ['id', 51736], ['id', 24462], ['id', 47914], ['ood', 34301], ['id', 19892], ['id', 13709], ['id', 57575], ['id', 29713], ['id', 36839], ['id', 2443], ['id', 26966], ['id', 49889], ['id', 43998], ['id', 29185], ['id', 23490], ['id', 36766], ['id', 53976], ['id', 56323], ['id', 53693]], 'labels': [9, 5, 2, 0, 9, 5, 6, 0, 0, 5, 4, 7, 0, 7, 3, 3, 6, 9, 9, 4], 'scores': [0.4663665294647217, 0.771243155002594, 0.7175777554512024, 0.7377856969833374, 0.4597729444503784, 0.48884856700897217, 0.6891185641288757, 0.4724200367927551, 0.5456319451332092, 0.6618884801864624, 0.5037789940834045, 0.8259299397468567, 0.8738375306129456, 0.533194899559021, 0.45992904901504517, 0.8265456557273865, 0.4255181849002838, 0.7297327518463135, 0.3832065463066101, 0.7228419780731201]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0322941541671753})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.511182963848114})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37749043107032776})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33215904235839844})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32946354150772095})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33998924493789673})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.328666627407074})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31530338525772095})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35519737005233765})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3315628170967102})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3568761944770813})
store['active_learning_steps'][15]['training']['best_epoch']=8
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.2502685546875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 14649], ['id', 55314], ['id', 27374], ['id', 2381], ['id', 2320], ['id', 21395], ['id', 54212], ['id', 49656], ['id', 40466], ['id', 3374], ['id', 30662], ['id', 55001], ['id', 11734], ['id', 30493], ['id', 32573], ['id', 52306], ['id', 49844], ['id', 41016], ['id', 14749], ['id', 46412]], 'labels': [0, 6, 2, 7, 6, 8, 7, 9, 8, 9, 3, 2, 8, 1, 8, 8, 9, 5, 0, 0], 'scores': [0.8521773219108582, 0.8336222171783447, 0.7449384331703186, 0.7990026473999023, 0.5506635904312134, 0.7731314301490784, 0.6531549692153931, 0.7327183485031128, 0.8340420722961426, 0.8357405662536621, 0.390924796462059, 0.5553221702575684, 0.7160077095031738, 0.6136317849159241, 0.7195642590522766, 0.8917389512062073, 0.5087226927280426, 0.5222892761230469, 0.9002770185470581, 0.6843975782394409]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0897444486618042})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.530484676361084})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35927337408065796})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3887884020805359})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3914549946784973})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3465920090675354})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3483310043811798})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3139926791191101})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3223837912082672})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35067397356033325})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3547744154930115})
store['active_learning_steps'][16]['training']['best_epoch']=8
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.2547722412109375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 46088], ['id', 40076], ['id', 15715], ['id', 18739], ['id', 38165], ['id', 38698], ['id', 55902], ['id', 38608], ['id', 5013], ['id', 15848], ['id', 35062], ['id', 40720], ['id', 59339], ['id', 28617], ['id', 31301], ['id', 51004], ['id', 42687], ['id', 34829], ['id', 47506], ['id', 34739]], 'labels': [6, 2, 2, 3, 5, 5, 5, 5, 2, 3, 5, 3, 1, 5, 5, 7, 5, 5, 8, 9], 'scores': [0.8751424551010132, 0.7205723524093628, 0.4249058961868286, 0.9313391149044037, 0.8131777048110962, 0.7657784819602966, 0.5367314219474792, 0.5840412974357605, 0.8720536231994629, 1.07571679353714, 0.5520468950271606, 0.6181761026382446, 0.6460394263267517, 0.6308802366256714, 0.7748327255249023, 0.6719073057174683, 0.6395267844200134, 0.9150596261024475, 0.7534101009368896, 0.6120426058769226]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0215497016906738})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5596931576728821})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4022061824798584})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33222776651382446})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3145129382610321})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3048672676086426})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30639275908470154})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31850117444992065})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3477722406387329})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.2490640380859375}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 5103], ['id', 29711], ['id', 19501], ['id', 52887], ['id', 48973], ['id', 34058], ['id', 42199], ['id', 23516], ['id', 33150], ['id', 24684], ['id', 45048], ['id', 13093], ['id', 41540], ['id', 39818], ['id', 938], ['id', 4955], ['ood', 19379], ['id', 33505], ['ood', 55531], ['id', 29132]], 'labels': [2, 8, 3, 1, 8, 3, 3, 5, 8, 9, 4, 3, 2, 1, 2, 2, 5, 2, 5, 8], 'scores': [0.8905112147331238, 0.6449729800224304, 0.6478975415229797, 0.5672231316566467, 0.7348344326019287, 0.7475557327270508, 0.884777843952179, 0.3578852117061615, 0.6857745051383972, 0.6533343195915222, 0.7571327686309814, 0.6130143404006958, 0.6533619165420532, 0.6686146259307861, 0.29167650640010834, 0.8633257746696472, 0.42442506551742554, 0.7186249494552612, 0.47102653980255127, 0.6341484785079956]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0549967288970947})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5163905024528503})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3810564875602722})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33425790071487427})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29245227575302124})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2821158766746521})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2778990864753723})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3045507073402405})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26969796419143677})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27806350588798523})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2867971658706665})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27100491523742676})
store['active_learning_steps'][18]['training']['best_epoch']=9
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9733, 'crossentropy': 0.24221865234375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 46122], ['id', 45424], ['id', 29903], ['id', 39412], ['id', 31197], ['id', 29], ['id', 49910], ['id', 25986], ['id', 9557], ['id', 12650], ['id', 17517], ['id', 29967], ['id', 21348], ['id', 20578], ['ood', 56233], ['id', 9567], ['id', 57319], ['id', 39499], ['id', 36508], ['id', 892]], 'labels': [2, 4, 0, 3, 2, 7, 6, 8, 8, 5, 9, 2, 6, 8, 5, 8, 2, 8, 5, 6], 'scores': [0.7785808444023132, 0.6921223104000092, 0.7925800085067749, 0.5524925291538239, 0.7654100060462952, 0.5984823703765869, 0.9071996212005615, 0.8189789652824402, 0.8240768611431122, 0.8175375461578369, 0.6601607203483582, 0.7087933421134949, 0.5517072081565857, 0.6632638573646545, 0.48022961616516113, 0.7841276526451111, 0.8426947593688965, 0.649912416934967, 0.8309548497200012, 0.6350737810134888]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.2112656831741333})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5566275119781494})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.37187111377716064})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3503696322441101})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31671684980392456})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2857118844985962})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2714248299598694})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27482175827026367})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26976191997528076})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30913111567497253})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28625261783599854})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.275662362575531})
store['active_learning_steps'][19]['training']['best_epoch']=9
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9713, 'crossentropy': 0.241352099609375}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 45617], ['id', 4317], ['id', 30157], ['id', 48158], ['id', 5082], ['id', 17244], ['id', 18324], ['id', 1674], ['id', 17209], ['id', 49515], ['id', 34071], ['id', 17792], ['id', 1812], ['id', 42004], ['id', 12970], ['id', 23927], ['id', 10824], ['id', 51764], ['id', 53754], ['id', 55496]], 'labels': [0, 7, 6, 2, 0, 8, 0, 9, 1, 2, 6, 9, 4, 7, 7, 5, 2, 5, 6, 9], 'scores': [0.46661388874053955, 0.7077009677886963, 0.7724238634109497, 0.6763306856155396, 0.6085383892059326, 0.4931730031967163, 0.9644143581390381, 0.8397603034973145, 0.45499444007873535, 0.7725821733474731, 0.6780660152435303, 0.7405855655670166, 0.7441542148590088, 0.7245948314666748, 0.6182995438575745, 0.5665092468261719, 0.5342429280281067, 0.9614484906196594, 0.4848251938819885, 0.7292568683624268]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.3063368797302246})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6492174863815308})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.44971734285354614})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3125094771385193})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2780943512916565})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2806416153907776})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24709045886993408})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2450290322303772})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24524995684623718})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.284894198179245})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2558886408805847})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.239315234375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 7192], ['id', 43176], ['id', 52392], ['id', 32288], ['id', 2148], ['id', 40268], ['id', 52550], ['id', 3810], ['id', 37403], ['id', 15855], ['id', 14697], ['id', 52225], ['id', 134], ['id', 8202], ['id', 11536], ['id', 54973], ['id', 44534], ['id', 23968], ['id', 7265], ['id', 3626]], 'labels': [3, 2, 1, 2, 6, 5, 2, 3, 2, 5, 8, 2, 1, 2, 9, 2, 9, 7, 2, 3], 'scores': [0.7841541469097137, 0.657179594039917, 0.7618187069892883, 0.46765708923339844, 0.7342010140419006, 0.5484026074409485, 0.6349655091762543, 0.8418579697608948, 0.8076560497283936, 0.7591128349304199, 0.7864134907722473, 0.949251115322113, 0.9379720091819763, 0.6582476496696472, 0.6383447647094727, 0.5813032686710358, 0.7957372069358826, 0.6331533193588257, 0.646251916885376, 0.6097934246063232]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0441648960113525})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.530470609664917})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36862510442733765})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3320513963699341})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26848646998405457})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2502795457839966})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2369072437286377})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2541930377483368})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.24329447746276855})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.23789164423942566})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.974, 'crossentropy': 0.241445849609375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 17876], ['id', 45911], ['id', 30016], ['ood', 29611], ['id', 56480], ['id', 1872], ['id', 17060], ['id', 10256], ['id', 20641], ['id', 36434], ['id', 57665], ['id', 29294], ['id', 24589], ['id', 13524], ['id', 6839], ['id', 33338], ['id', 52644], ['id', 20037], ['id', 35482], ['id', 48912]], 'labels': [6, 3, 4, 5, 9, 3, 8, 2, 9, 4, 8, 3, 8, 3, 2, 8, 7, 8, 4, 2], 'scores': [0.570038378238678, 0.5831987857818604, 0.7838391065597534, 0.41673874855041504, 0.6970218420028687, 0.5941033959388733, 0.4022264778614044, 0.48662278056144714, 0.8867389559745789, 0.6878637671470642, 0.7788630723953247, 0.6440027952194214, 0.7833775877952576, 0.9348919987678528, 0.6037026047706604, 0.7570967674255371, 0.81346595287323, 0.8028115630149841, 0.7102111577987671, 0.7439817190170288]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1651628017425537})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.6037082076072693})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4323080778121948})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3131292462348938})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2762297987937927})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24422918260097504})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24378666281700134})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.23957082629203796})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24540400505065918})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26072824001312256})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27550360560417175})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9759, 'crossentropy': 0.2362485107421875}
