store = {}
store['timestamp']=1621471670
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=26']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=26
store['worker_id']=26
store['num_workers']=80
store['config']={'seed': 1261, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.2005574703216553})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.4250848293304443})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.841845989227295})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6365866661071777})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6956, 'crossentropy': 2.0028982421875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 36122], ['id', 57523], ['id', 39442], ['id', 47651], ['id', 37181]], 'labels': [9, 3, 8, 3, 5], 'scores': [1.217751699140472, 2.2401925790247286, 2.9874956604047913, 3.5326811515772167, 3.908696798001772]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.9730727672576904})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.400585174560547})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.6200170516967773})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.707446575164795})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.6816694736480713})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 3.1125688552856445})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.6971611976623535})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.716, 'crossentropy': 2.4899001953125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 32022], ['id', 12196], ['id', 33832], ['id', 15753], ['id', 53989]], 'labels': [2, 2, 2, 0, 2], 'scores': [1.2772996113705266, 2.3715343281718697, 3.2410746925561966, 3.8031250279621265, 4.153939326754697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.8990757465362549})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.180716037750244})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.2012081146240234})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.1532468795776367})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.674180030822754})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.5457029342651367})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.7146596908569336})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7235, 'crossentropy': 1.98183203125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 19042], ['id', 14397], ['id', 13460], ['id', 37453], ['id', 46476]], 'labels': [9, 4, 5, 5, 5], 'scores': [1.255846244276725, 2.3014929277322054, 3.1508275842020153, 3.71905480526285, 4.099250766030721]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.0083794593811035})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.3386428356170654})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.1738860607147217})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.698302745819092})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.5179219245910645})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.546091079711914})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.8457703590393066})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.3652310371398926})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7257, 'crossentropy': 2.1401501953125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 7990], ['id', 1589], ['id', 30398], ['id', 27223], ['id', 57305]], 'labels': [6, 7, 3, 2, 1], 'scores': [1.1569819689604746, 2.2051060730535914, 3.059511441766313, 3.676442787348847, 4.0813379464741315]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.3421272039413452})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.4693644046783447})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.6389853954315186})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.5495232343673706})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.9045088291168213})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.6441385746002197})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.7250570058822632})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8026, 'crossentropy': 1.3421779296875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 49438], ['id', 42383], ['id', 22480], ['id', 23877], ['id', 7833]], 'labels': [8, 8, 4, 3, 5], 'scores': [1.1581370969208744, 2.186996730541007, 3.042439705049878, 3.641605674378426, 4.046507547623428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.4170053005218506})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.748004674911499})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.8760746717453003})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.0256905555725098})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.0371382236480713})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7869, 'crossentropy': 1.450951171875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 28313], ['id', 42004], ['id', 22083], ['id', 52151], ['id', 27498]], 'labels': [9, 7, 2, 9, 7], 'scores': [1.1147665233453334, 2.1211534289482374, 2.9016053369502384, 3.4856106914677962, 3.902302390026117]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.3726649284362793})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.433567762374878})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.7094780206680298})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.61250638961792})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.802262783050537})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.8072195053100586})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.7679617404937744})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.876427173614502})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.9742153882980347})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 2.0806126594543457})
store['active_learning_steps'][6]['training']['best_epoch']=7
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7989, 'crossentropy': 1.5781015625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 39963], ['id', 17755], ['id', 41911], ['id', 50006], ['id', 24716]], 'labels': [4, 0, 2, 5, 5], 'scores': [1.2553521888682078, 2.345878830946408, 3.2308808827617526, 3.8302489744970156, 4.1895207109773915]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.6428803205490112})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.941049337387085})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.8976759910583496})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 2.1058249473571777})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 2.018918514251709})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 2.190180540084839})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.9584976434707642})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8083, 'crossentropy': 1.65847109375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 39407], ['id', 16860], ['id', 14100], ['id', 50403], ['id', 4646]], 'labels': [0, 8, 5, 3, 2], 'scores': [1.3572462779185046, 2.358316273574649, 3.177045109913169, 3.7475302698670445, 4.112252792907878]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.271173119544983})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.4045698642730713})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.7117174863815308})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.6035250425338745})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.9131734371185303})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 2.1794238090515137})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.814, 'crossentropy': 1.3383517578125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 35401], ['id', 42515], ['id', 50858], ['id', 15191], ['id', 7214]], 'labels': [3, 8, 4, 0, 3], 'scores': [1.0517352337259467, 1.9941232892682144, 2.7864682972939816, 3.401464402248725, 3.8374620402743993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.1897846460342407})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.5710300207138062})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.6002358198165894})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.7670495510101318})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.755030870437622})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.637624740600586})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.8981773853302002})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.9839491844177246})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.8618059158325195})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 2.1881399154663086})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.9971723556518555})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 2.049455404281616})
store['active_learning_steps'][9]['training']['best_epoch']=9
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.828, 'crossentropy': 1.598951171875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 45602], ['id', 24412], ['id', 32323], ['id', 24424], ['id', 40093]], 'labels': [5, 7, 5, 1, 6], 'scores': [1.2312049064986161, 2.359998798748224, 3.219325733174596, 3.8322750427242838, 4.2106855996347115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.3028604984283447})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.4666309356689453})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.6255621910095215})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.4676405191421509})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.6506497859954834})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.6941533088684082})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.7648870944976807})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.6883896589279175})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8425, 'crossentropy': 1.29077412109375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 57972], ['id', 8691], ['id', 8031], ['id', 14705], ['id', 8516]], 'labels': [4, 2, 8, 0, 7], 'scores': [1.160339054560302, 2.2207559486778417, 3.0877222445047057, 3.7113866481969247, 4.12420303748136]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.05904221534729})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.2309449911117554})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.164078950881958})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3132623434066772})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.3943700790405273})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.393484354019165})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.4685882329940796})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.5519273281097412})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8666, 'crossentropy': 1.08241201171875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 6130], ['id', 4822], ['id', 36078], ['id', 20170], ['id', 23386]], 'labels': [7, 4, 3, 9, 7], 'scores': [1.2351814297702162, 2.326095161375932, 3.215848145226367, 3.8275188712005797, 4.212705860513591]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0056157112121582})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1125510931015015})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1745505332946777})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.4298527240753174})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.3478697538375854})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3843131065368652})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.858, 'crossentropy': 0.95076162109375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 59726], ['id', 6604], ['id', 40466], ['id', 21532], ['id', 53504]], 'labels': [5, 8, 8, 5, 2], 'scores': [1.0593293116917573, 2.012532591135042, 2.8226451835206428, 3.453884288575715, 3.8938985761346974]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.0899757146835327})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.216253399848938})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2562062740325928})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.4041757583618164})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.3645789623260498})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.5402754545211792})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.7994887828826904})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.4541802406311035})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.388635277748108})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.4237126111984253})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.7771377563476562})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.581050157546997})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.573961853981018})
store['active_learning_steps'][13]['training']['best_epoch']=10
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8699, 'crossentropy': 1.19553037109375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 13156], ['id', 39822], ['id', 30322], ['id', 40624], ['id', 49563]], 'labels': [2, 9, 8, -1, 8], 'scores': [1.2184549107486906, 2.345566760083531, 3.2409587369437016, 3.8469634649853557, 4.20237266475887]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.1776130199432373})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9732500314712524})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3220245838165283})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.3001381158828735})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.5159708261489868})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8615, 'crossentropy': 0.85105390625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 7033], ['id', 25384], ['id', 50403], ['id', 31624], ['id', 57728]], 'labels': [7, 5, -1, 9, 9], 'scores': [1.0070872642228723, 1.917166612824575, 2.725839831758905, 3.3232364405798034, 3.77802828223511]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.2660198211669922})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9880670309066772})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0753636360168457})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1869900226593018})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2344446182250977})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3183188438415527})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8609, 'crossentropy': 0.89585654296875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 17870], ['id', 20322], ['id', 19942], ['id', 57628], ['id', 39830]], 'labels': [4, 1, 5, 2, 1], 'scores': [1.0445126648217467, 2.00271373526272, 2.816639858077071, 3.4305793063342076, 3.867041127258698]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.1168839931488037})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1739258766174316})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.2966761589050293})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.4548184871673584})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.4496119022369385})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.6282188892364502})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.5648598670959473})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8463, 'crossentropy': 1.1809642578125}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 49497], ['id', 43998], ['id', 40775], ['id', 57463], ['id', 32738]], 'labels': [0, 7, 6, 6, 7], 'scores': [1.1504147700447103, 2.1282616692634067, 2.9458162119622013, 3.548151539339453, 3.9627456839575874]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9689502716064453})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9031448364257812})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9134277105331421})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0567500591278076})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0284912586212158})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2549439668655396})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2521536350250244})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8734, 'crossentropy': 0.88122099609375}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 12647], ['id', 20832], ['id', 42415], ['id', 34758], ['id', 50320]], 'labels': [1, 2, 7, 8, 5], 'scores': [1.0781111634824487, 2.0557764420351265, 2.8828824946832405, 3.519529086263744, 3.945992402599413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9815176725387573})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9133747816085815})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9636833071708679})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9882373809814453})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0588103532791138})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.1455121040344238})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0321242809295654})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8969, 'crossentropy': 0.753665478515625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 36744], ['id', 7168], ['id', 14305], ['id', 25960], ['id', 52688]], 'labels': [1, 8, 8, 4, 6], 'scores': [1.095563109699214, 2.099728328946252, 2.922780756257527, 3.5376528882975347, 3.9540273954272687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0590274333953857})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7474528551101685})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8200230598449707})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9730744957923889})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8443397283554077})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9600101709365845})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9076876044273376})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9227131605148315})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8954, 'crossentropy': 0.769217138671875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 46530], ['id', 12663], ['id', 15855], ['id', 8821], ['id', 31184]], 'labels': [4, 8, 5, 3, 9], 'scores': [1.120920733700296, 2.0829282886607596, 2.9228388202696944, 3.559702737622519, 3.991699120217829]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.888333797454834})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6975358128547668})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7872083187103271})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7171399593353271})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8203248977661133})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7648234963417053})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8291954398155212})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9819352030754089})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8600404262542725})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.652578466796875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 43575], ['id', 17756], ['id', 14317], ['id', 36818], ['id', 20150]], 'labels': [2, 8, 9, 7, 3], 'scores': [1.2190978336033667, 2.275998870199978, 3.133506101823304, 3.742060909907659, 4.118296786452622]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9836400151252747})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7143189907073975})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8371031284332275})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8421391248703003})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8578834533691406})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9004507064819336})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9138557314872742})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8469842672348022})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.6628927734375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 5684], ['id', 266], ['id', 24457], ['id', 44898], ['id', 12650]], 'labels': [6, 5, 8, 2, 5], 'scores': [1.0969570442775554, 2.100613384716829, 2.9551528358230854, 3.6110979186845755, 4.0297365006258214]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9881411790847778})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7821699380874634})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7964092493057251})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.705313503742218})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7754185199737549})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9103338718414307})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8687024116516113})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8999, 'crossentropy': 0.639420263671875}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 5600], ['id', 59314], ['id', 29132], ['id', 49204], ['id', 14655]], 'labels': [6, 9, 8, 9, 3], 'scores': [1.0652125078550423, 2.0578694080916904, 2.880155486242651, 3.4961602327284407, 3.917363591363854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0661711692810059})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6901419162750244})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6554906368255615})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7324983477592468})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6855156421661377})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7103652954101562})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8738197088241577})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8518196940422058})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7571889758110046})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.914, 'crossentropy': 0.601794580078125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 58560], ['id', 37465], ['id', 59934], ['id', 23422], ['id', 9608]], 'labels': [0, 5, 0, 8, 8], 'scores': [1.1373655709837545, 2.219005200549061, 3.0734079977955515, 3.6709778499431582, 4.048657604661628]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9848647117614746})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7145600318908691})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7679619789123535})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6979391574859619})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7251602411270142})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7631843090057373})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8456201553344727})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7429401874542236})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8133672475814819})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7963427305221558})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8657509088516235})
store['active_learning_steps'][24]['training']['best_epoch']=8
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.66706064453125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 35864], ['id', 57507], ['id', 8879], ['id', 13752], ['id', 49354]], 'labels': [5, 0, 3, 9, 0], 'scores': [1.1366632989236427, 2.192177817693369, 3.0427757614333366, 3.6694538061454436, 4.0849864600214385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0250399112701416})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7046130895614624})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6607176661491394})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.685592532157898})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7606217861175537})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7077343463897705})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8032519221305847})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8015635013580322})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7912031412124634})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9196, 'crossentropy': 0.623339453125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 53693], ['id', 3719], ['id', 28930], ['id', 18487], ['id', 32427]], 'labels': [4, 2, 7, 4, 0], 'scores': [1.1194171533731103, 2.145922007693403, 2.998545515872019, 3.642262001392486, 4.052228512030567]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.179530143737793})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7245944738388062})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6802577972412109})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7022709846496582})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6871012449264526})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7168015241622925})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6928061246871948})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8139067888259888})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7977492213249207})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9289859533309937})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9239, 'crossentropy': 0.596784033203125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 29335], ['id', 26079], ['id', 53872], ['id', 52358], ['id', 5851]], 'labels': [8, 8, 8, 2, 7], 'scores': [1.1861874092853855, 2.176598154537543, 3.0348876461978715, 3.6410299375232285, 4.03472858658707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.1399853229522705})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6651284694671631})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6519392728805542})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5596274733543396})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5817601084709167})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6220992803573608})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7146059274673462})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9251, 'crossentropy': 0.521271875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 44172], ['id', 40976], ['id', 17540], ['id', 34328], ['id', 52514]], 'labels': [8, 1, 1, 8, 6], 'scores': [0.9771869774357009, 1.867940426504692, 2.6454970860235143, 3.284430601792331, 3.7492520874213504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1999226808547974})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6074485778808594})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5721544027328491})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5793718099594116})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6022385954856873})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5696326494216919})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9264, 'crossentropy': 0.5094546875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 39480], ['id', 28512], ['id', 6466], ['id', 26072], ['id', 8214]], 'labels': [9, 5, 2, 1, 7], 'scores': [0.8756526172826056, 1.7019980274240591, 2.425487612619918, 3.044016960568408, 3.5366471384737848]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.2063413858413696})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6510715484619141})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5863189697265625})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5613153576850891})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5883985161781311})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6304427981376648})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5944125056266785})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6520569324493408})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6283783912658691})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.667863130569458})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6278359293937683})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9397, 'crossentropy': 0.5741341796875}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 9180], ['id', 35652], ['id', 635], ['id', 40654], ['id', 12089]], 'labels': [3, 2, 5, 5, 3], 'scores': [1.2337299141684794, 2.3463304978153405, 3.237249251743899, 3.822820402087954, 4.171830427815603]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.1846987009048462})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5670516490936279})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5819908380508423})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5229592323303223})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5565974712371826})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5312967300415039})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.557766854763031})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6038739681243896})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5955810546875})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9369, 'crossentropy': 0.47552041015625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 52099], ['id', 20859], ['id', 17494], ['id', 11292], ['id', 50317]], 'labels': [2, 8, 5, 1, 3], 'scores': [1.1076373145382221, 2.0818544500390326, 2.911266520224192, 3.546970950174673, 3.985988511732125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2883487939834595})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6672748923301697})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.605707049369812})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5470378994941711})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5693084597587585})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5518845319747925})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5494160652160645})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6253905296325684})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9321, 'crossentropy': 0.517748193359375}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 42703], ['id', 48010], ['id', 35326], ['id', 57474], ['id', 24632]], 'labels': [0, 7, 5, 3, 2], 'scores': [1.148552799853921, 2.0819528440881143, 2.85782120976806, 3.4672644787644096, 3.8911360812594618]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.1735361814498901})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6945674419403076})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5409297347068787})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5608614683151245})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5583639144897461})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5484552979469299})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6342174410820007})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9339, 'crossentropy': 0.497892578125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 43745], ['id', 52294], ['id', 50403], ['id', 45944], ['id', 17808]], 'labels': [8, 0, -1, 9, 8], 'scores': [0.9310941891762585, 1.8149204707587332, 2.58063787108125, 3.2044809495647018, 3.6713978672592535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.089097499847412})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5990725755691528})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5550327897071838})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5719863772392273})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5727748274803162})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5141671895980835})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6469411849975586})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5962109565734863})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5764423608779907})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6460474729537964})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6559290289878845})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6969919204711914})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9387, 'crossentropy': 0.509346533203125}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 49282], ['id', 424], ['id', 20169], ['id', 36363], ['id', 58832]], 'labels': [2, 9, 4, 6, 3], 'scores': [1.1389196520231706, 2.168790839137729, 3.027075480432, 3.6392221821865753, 4.039567420525866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.158714771270752})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5968509912490845})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5468990206718445})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4966360330581665})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5071092844009399})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5687577128410339})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5373939275741577})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49424973130226135})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9416, 'crossentropy': 0.45882841796875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 5013], ['id', 13195], ['id', 38420], ['id', 29662], ['id', 13942]], 'labels': [2, -1, 8, 2, 4], 'scores': [1.0777951799173637, 1.9884723201119794, 2.789730940803268, 3.4101862801530745, 3.856479423963812]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.240835189819336})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6256356239318848})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4932306110858917})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6539415121078491})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5365233421325684})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5578967332839966})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9348, 'crossentropy': 0.477538916015625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 1674], ['id', 40766], ['id', 37696], ['id', 13922], ['id', 39561]], 'labels': [9, 4, 2, 2, 2], 'scores': [0.882131626756461, 1.6819462631257802, 2.4204760381104027, 3.0183615422580656, 3.485118678211153]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.3289625644683838})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6979535818099976})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.561131477355957})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6043705344200134})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5796698927879333})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6097319722175598})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.52653623046875}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 37347], ['id', 41171], ['id', 33812], ['id', 32445], ['id', 31664]], 'labels': [2, 3, 6, 5, 3], 'scores': [0.8920867681679527, 1.6785861224506133, 2.399657146624479, 2.982275013152675, 3.4412836399800817]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.4122521877288818})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6461911201477051})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5605534315109253})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5415504574775696})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5743910670280457})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5293421745300293})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5350963473320007})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5481534004211426})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5433608889579773})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5659295320510864})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9427, 'crossentropy': 0.4759095703125}
